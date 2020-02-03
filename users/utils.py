import random




def weighted_choice(choices, size=1, unique=True):

    assert isinstance(choices, list)
    assert isinstance(size, int)
    assert isinstance(unique, bool)

    if len(choices) == 0:
        return []

    if size == 1:
        total = sum(w for c, w in choices)
        r = random.uniform(0, total)
        upto = 0
        for c, w in choices:
            if upto + w >= r:
                return [c]
            upto += w
        assert False
    elif size > 1:
        choice = weighted_choice(choices=choices, size=1, unique=unique)
        if unique:
            new_choices = [(c, w) for c, w in choices if c != choice[0]]
        else:
            new_choices = choices
        return choice + weighted_choice(choices=new_choices, size=size-1, unique=unique)



def people(request, product=None, categories=None):
    crosssells = []
    probabilities = []
    ranks = []
    session = {}
    ads = Product.objects.filter(orderable=True, public=True, searchable=True, image__isnull=False, ad_weight__isnull=False, ad_weight__gt=0)
    if product and not categories:
        categories = product.categories.all()
    if categories:
        ads = ads.filter(categories__in=categories)
    ads = ads.order_by('?')[:30]
    choices = []

    # Retrieve the session
    if 'product_adranks' in request.session:
        session = request.session['product_adranks'].copy()

    for ad in ads:
        rank = ad.ad_weight
        if ad.id in session:
            rank += session[ad.id]
        if product:
            adrank = None
            adrank = ProductAdRank.objects.get(product=product, ad=ad)
            if adrank:
                rank += adrank.rank
        choices.append((ad, rank))

    crosssells = weighted_choice(choices=choices, size=4, unique=True)
