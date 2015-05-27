from joins.models import Join


class ReferMiddleware():
    """ docstring for ReferMiddleware:
        The purpose of this middleware class
        is to handle a reference parameter
        in page links
        This is how we track who sent someone to
        sign up with the site.
    """

    def process_request(self, request):
        # parse request for reference parameter
        ref_id = request.GET.get("ref")
        # process the ref param
        print ref_id

        try:
            obj = Join.objects.get(ref_id=ref_id)
        except:
            obj = None

        if obj:
            request.session['ref'] = obj.id
