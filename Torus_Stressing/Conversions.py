from decimal import Decimal, getcontext, ROUND_HALF_UP
import Formulas
import math

getcontext().prec = 28
pi = Decimal(math.pi)


def inch_to_meter(inches):
    return Formulas.round_floating_point(Decimal(inches * 0.0254))


def inch_to_feet(inches):
    return Formulas.round_floating_point(Decimal(inches * 12))


def feet_to_inch(feet):
    return Formulas.round_floating_point(Decimal(feet / 12)
    )


def meter_to_feet(meter):
    return Formulas.round_floating_point(Decimal(meter / Decimal(0.0254 * 12)))


def linear_to_rpm(total_radius, linear_speed):
    rpm = Decimal(linear_speed * 60) / Decimal(2 * total_radius * pi)

    return Formulas.round_floating_point(rpm)


def rpm_to_linear(total_radius, rpm):
    linear = Decimal(rpm * 2 * total_radius * pi) / Decimal(60)

    return Formulas.round_floating_point(linear)


def rpm_to_angular(rpm):
    angular = (Decimal(2) * pi * rpm) / 60

    return Formulas.round_floating_point(angular)


def g_cm3_to_kg_m3(g_cm3):
    kg_m3 = Decimal(1000) * g_cm3

    return Formulas.round_floating_point(kg_m3)

