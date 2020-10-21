from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.decorators.http import require_POST
from coupons.models import Coupon
from coupons.forms import CouponApplyForm
from django.contrib import messages


@require_POST
def coupon_apply(request):
    now = timezone.now()
    form = CouponApplyForm(request.POST)

    if form.is_valid():
        code = form.cleaned_data["code"]

        try:
            coupon = Coupon.objects.get(
                code__iexact=code, valid_from__lte=now, valid_to__gte=now, active=True
            )
            request.session["coupon_id"] = coupon.id
            messages.success(request, "Kupon sikeresen beváltva")
        except Coupon.DoesNotExist:
            request.session["coupon_id"] = None
            messages.warning(request, "Kupon nem letezik")
    return redirect("cart:cart_detail")

