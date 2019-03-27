import math
import Main
from decimal import Decimal, getcontext, ROUND_HALF_UP

getcontext().prec = 28
pi = Decimal(math.pi)


# Use decimal module to retain precision
def area_of_circle(radius):
    if radius <= 0:
        raise ArithmeticError('Radius is less then or equal to zero')

    area = pi * Decimal(radius ** Decimal(2))

    return round_floating_point(area)


def circumference_of_circle(radius):
    if radius <= 0:
        raise ArithmeticError('Radius is less then or equal to zero')

    circumference = pi * Decimal(radius * Decimal(2))

    return round_floating_point(circumference)


def volume_of_sphere(radius):
    if radius <= 0:
        raise ArithmeticError('Radius is less then or equal to zero')

    volume = Decimal(4 / 3) * pi * Decimal(radius ** Decimal(3))

    return round_floating_point(volume)


def cross_section_hollow_torus(outer_radius, wall_thickness):
    if outer_radius <= 0 or wall_thickness <= 0:
        raise ArithmeticError('One of the passed arguments is less then or equal to zero')
    elif wall_thickness > outer_radius:
        raise ArithmeticError('Wall thickness greater than inner radius')

    cross_section = Decimal(area_of_circle(outer_radius)) - Decimal(area_of_circle(outer_radius - wall_thickness))

    return round_floating_point(cross_section)


def volume_of_solid_torus(total_radius, outer_radius):
    if total_radius <= 0 or outer_radius <= 0:
        raise ArithmeticError('One of the passed arguments is less then or equal to zero')

    volume = \
        Decimal(2) * Decimal(pi ** 2) * \
        Decimal(total_radius - outer_radius) * Decimal(outer_radius ** 2)

    return round_floating_point(volume)


def volume_of_hollow_torus(total_radius, outer_radius, wall_thickness):
    if total_radius <= 0 or outer_radius <= 0 or wall_thickness <= 0:
        raise ArithmeticError('One of the passed arguments is less then or equal to zero')

    volume = volume_of_solid_torus(total_radius, outer_radius - wall_thickness)

    if volume < 0:
        raise ArithmeticError(
            'Total radius to small in proportion to outer radius, 3D space overlap causes volume to '
            'come out as negative. Use alternative equation'
        )

    return round_floating_point(volume)


def volume_of_torus_wall(total_radius, outer_radius, wall_thickness):
    if total_radius <= 0 or outer_radius <= 0 or wall_thickness <= 0:
        raise ArithmeticError('One of the passed arguments is less then or equal to zero')

    volume = volume_of_solid_torus(total_radius, outer_radius) - \
        volume_of_solid_torus(total_radius, outer_radius - wall_thickness)

    if volume < 0:
        raise ArithmeticError(
            'Total radius to small in proportion to outer radius, 3D space overlap causes volume to '
            'come out as negative. Use alternative equation'
        )

    return round_floating_point(volume)


def linear_speed_rotational(total_radius, acceleration):
    if total_radius <= 0 or acceleration < 0:
        raise ArithmeticError('One of the passed arguments is less then or equal to zero')

    speed = Decimal(math.sqrt(acceleration * total_radius))

    return round_floating_point(speed)


def stress_on_torus(total_radius, outer_radius, wall_thickness, density_of_material, acceleration, additional_mass):
    if total_radius <= 0 or outer_radius <= 0 or wall_thickness < 0 or density_of_material < 0 or acceleration < 0:
        raise ArithmeticError('One of the passed arguments is less then or equal to zero')

    vol_of_walls = volume_of_torus_wall(total_radius, outer_radius, wall_thickness)
    cross_section = cross_section_hollow_torus(outer_radius, wall_thickness)

    newton_force = (Decimal(vol_of_walls) * Decimal(density_of_material) + additional_mass) * Decimal(acceleration)

    mpa = (Decimal(newton_force) / Decimal(cross_section)) / Decimal(1000000)

    return round_floating_point(mpa)


def get_sigfig(number):
    string = '{0:f}'.format(number)
    print(string)


def round_floating_point(num):
    return Decimal(num.quantize(
        Decimal(str(10 ** -Main.rounding_places)),
        rounding=ROUND_HALF_UP)
    )
