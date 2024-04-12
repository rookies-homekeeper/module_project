from django import template
from django.utils import timezone

register = template.Library()

@register.filter
def timesince_custom(value):
    """
    이 필터는 타임존을 고려하여 시간을 "1일 전", "2일 전" 등으로 표시합니다.
    """
    now = timezone.now()  # 현재 시간 (타임존 고려)

    # value가 타임존을 고려한 datetime 객체인지 확인
    if not timezone.is_aware(value):
        # value를 타임존이 있는 datetime 객체로 변환
        value = timezone.make_aware(value, timezone.get_current_timezone())

    # 현재 시간과의 차이 계산
    delta = now - value

    if delta.days == 0:
        return "오늘"
    elif delta.days == 1:
        return "1일 전"
    else:
        return "{}일 전".format(delta.days)

    return ""
