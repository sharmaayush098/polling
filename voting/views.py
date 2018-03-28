import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from voting.models import Votes, VoteDetail


@csrf_exempt
def voters(request, vote_id):
    if request.method == 'GET':
        try:
            vote_obj = VoteDetail.objects.get(id=vote_id)
            total_obj = Votes.objects.get(id=vote_id).total_votes

        except:
            vote_obj = VoteDetail.objects.create(id=vote_id)
        return render(request, 'voting_page.html', {"vote_obj": vote_obj, "total_obj": total_obj})
    if request.method == 'POST':
        try:
            vote_obj = VoteDetail.objects.get(id=int(vote_id))
            total_obj = Votes.objects.get(id=vote_id)


        except:
            vote_obj = None
        if vote_obj:
            vote_obj.voted += 1
            vote_obj.save()
            voted = vote_obj.voted
            not_voted = vote_obj.not_voted
            total_obj.total_votes = voted + not_voted

        else:
            vote_obj = VoteDetail.objects.create(voted=1)

            voted = vote_obj.voted
            not_voted = vote_obj.not_voted
            total_obj.total_votes = voted + not_voted
        return HttpResponse(content_type='application/json', content=json.dumps({"vote_yes": voted,
                                                                                 "total_votes": total_obj.total_votes,
                                                                                "vote_no": not_voted}))
@csrf_exempt
def devoters(request, vote_id):
        if request.method == 'GET':
            try:
                vote_obj = VoteDetail.objects.get(id=vote_id)
                total_obj = Votes.objects.get(id=vote_id).total_votes
            except:
                vote_obj = VoteDetail.objects.create(id=vote_id)
            return render(request, 'voting_page.html', {"vote_obj": vote_obj, "total_obj": total_obj})
        if request.method == 'POST':
            try:
                vote_obj = VoteDetail.objects.get(id=int(vote_id))
                total_obj = Votes.objects.get(id=vote_id)
            except:
                vote_obj = None
            if vote_obj:
                vote_obj.not_voted += 1
                vote_obj.save()
                not_vote = vote_obj.not_voted
                voted = vote_obj.voted
                total_obj.total_votes = not_vote + voted
            else:
                vote_obj = VoteDetail.objects.create(voted=1)

                voted = vote_obj.voted
                not_voted = vote_obj.not_voted
                total_obj.total_votes = voted + not_voted

        return HttpResponse(content_type='application/json', content=json.dumps({"vote_yes": voted,
                                                                                 "total_votes": total_obj.total_votes,
                                                                                "vote_no": not_vote}))













