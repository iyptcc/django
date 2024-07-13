from datetime import date

from django.contrib import messages
from django.utils.safestring import mark_safe

from apps.dashboard.tasks import Task, TaskList
from apps.registration.models import Application


def todos(sender, **kwargs):
    request = kwargs["context"]["request"]
    if request.user.is_authenticated:
        if not request.user.first_name or not request.user.last_name:
            sender.add_task(Task("Set first and last name", 0, url="account:profile"))
        if (
            not request.user.profile.tournament
            and request.user.profile.attendee_set.count() > 0
        ):
            sender.add_task(Task("Set active tournament", 0, url="account:tournament"))
            messages.add_message(
                request,
                messages.WARNING,
                mark_safe(
                    "You have no active Tournament selected. Set one <a href='/account/tournament/'>here</a>"
                ),
            )
        if (
            not request.user.profile.tournament
            and request.user.profile.attendee_set.count() == 0
            and request.user.profile.application_set.count() == 0
        ):
            sender.add_task(
                Task(
                    "Apply for participation in a tournament",
                    0,
                    url="registration:applications",
                )
            )

        if request.user.profile.attendee_set.filter(
            tournament=request.user.profile.tournament
        ).exists():
            if (
                request.user.profile.tournament.date_end is not None
                and request.user.profile.tournament.date_end < date.today()
            ):
                mytrns = ", ".join(
                    request.user.profile.tournaments.filter(
                        date_end__gt=date.today()
                    ).values_list("name", flat=True)
                )
                applied = ", ".join(
                    Application.objects.filter(applicant=request.user.profile)
                    .values_list("tournament__name", flat=True)
                    .distinct()
                )

                messages.add_message(
                    request,
                    messages.WARNING,
                    mark_safe(
                        f"""<h4>You are operating in a past tournament!</h4>
                                                    <p>Please select a current tournament from ({mytrns}) <a href='/account/tournament/'>here</a> or,</p>
                                                    <p>you can apply for a new tournament <a href='/registration/list/'>here</a> (you already applied to : {applied}).</p>"""
                    ),
                )

            real = False
            for role in request.user.profile.attendee_set.get(
                tournament=request.user.profile.tournament
            ).roles.all():
                if role.attending:
                    real = True
            if not real:
                messages.add_message(
                    request,
                    messages.WARNING,
                    mark_safe(
                        """<h4>The roles with which you hold do not qualify to attend the tournament!</h4>
                                                    <p>If you plan to attend the tournament, please apply for a suitable additional role.</p>
                                                    <p>This issue is mainly for team managers, which are per default not attending. In this case, become a team leader or apply as experienced juror.</p>"""
                    ),
                )


TaskList.show_signal.connect(todos)
