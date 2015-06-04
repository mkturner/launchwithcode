
from django.shortcuts import render, HttpResponseRedirect, Http404

from .forms import EmailForm, JoinForm
from .models import Join


# Create your views here.
def get_ip(request):
    try:
        x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forward:
            ip = x_forward.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
    except:
        ip = ""

    return ip

import uuid


def get_ref_id():
    ref_id = str(uuid.uuid4())[:11].replace('-', '').lower()
    try:
        id_exists = Join.objects.get(ref_id=ref_id)
        get_ref_id()
    except:
        return ref_id


def share(request, ref_id):
    # print ref_id
    try:
        join_obj = Join.objects.get(ref_id=ref_id)
        friends_referred = Join.objects.filter(friend=join_obj)
        count = join_obj.referral.all().count()
        ref_url = "http://launch.geakd.com/?ref=%s" % (join_obj.ref_id)
        context = {"ref_id": join_obj.ref_id, "count": count, "ref_url":
                   ref_url}
        template = "share.html"
        return render(request, template, context)
    except:
        raise Http404


def home(request):
    try:
        join_id = request.session['join_id_ref']
        obj = Join.objects.get(id=join_id)
        print ("the id is %s" % (join_id))
    except:
        obj = None

    # Using model forms
    form = JoinForm(request.POST or None)

    if form.is_valid():
        new_join = form.save(commit=False)
        # commit=False used to not save yet
        email = form.cleaned_data['email']
        new_join_old, created = Join.objects.get_or_create(email=email)
        if created:
            new_join_old.ref_id = get_ref_id()
            # add friend who referred new member to our join model
            if obj is not None:
                new_join_old.friend = obj
            new_join_old.ip_address = get_ip(request)
            new_join_old.save()

        # print all 'friends' that came from main sharer
        print Join.objects.filter(friend=obj)
        print obj.referral.all()

        #redirect here
        return HttpResponseRedirect("/%s" % (new_join_old.ref_id))

        # when finished processing, now save with new_join.save()
        # new_join.ip_address = get_ip(request)
        # new_join.save()

    context = {'form': form}
    template = 'home.html'
    return render(request, template, context)
