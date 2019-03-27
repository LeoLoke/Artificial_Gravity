import Formulas, Conversions, Drawing
from Drawing import GraphType
from decimal import Decimal

rounding_places = 12
pretty_round = 4

superscript = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")

# In feet
ft_per_story = Decimal(12)


def run():

    # These have to be in meters
    total_radius = Decimal(30)
    outer_radius = Decimal(4)
    wall_thickness = Decimal(.0254 * 1)

    # m/s2
    acceleration = Decimal(9.81)

    # Must be in kilograms
    additional_mass = Decimal(100000)

    # Put in terms of g/cm3
    density_of_material = Decimal(2.84)  # g/cm3 Al alloy 2219
    density_of_material = Decimal(Conversions.g_cm3_to_kg_m3(density_of_material))

    # Max tensile strength of the material given in MPa
    tensile_strength = Decimal(290)

    # Find a lot of common variables which are used often in other equations
    linear_velocity = Formulas.linear_speed_rotational(total_radius, acceleration)
    rpm = Conversions.linear_to_rpm(total_radius, linear_velocity)
    volume_of_walls = Formulas.volume_of_torus_wall(total_radius, outer_radius, wall_thickness)

    # Calculate the stress on the torus in MPa
    stress = Formulas.stress_on_torus(
        total_radius, outer_radius, wall_thickness, density_of_material, acceleration, additional_mass
    )

    # Volume of torus wall
    print('Volume of torus wall(hollow): ' +
          str(round(volume_of_walls, pretty_round)) +
          ' m3'.translate(superscript)
          )

    # Internal volume of torus for thickness of wall
    print('Volume of torus (hollow): ' +
          str(round(Formulas.volume_of_hollow_torus(total_radius, outer_radius, wall_thickness), pretty_round)) +
          ' m3'.translate(superscript)
          )

    # Speed torus would have to spin linearly to achieve centripetal acceleration
    print('Linear speed: ' +
          str(round(linear_velocity, pretty_round)) +
          ' m/s'.translate(superscript)
          )

    # 2-3 rpm is optimal, 10 rpm max can be trained
    print('RPM: ' +
          str(round(Conversions.linear_to_rpm(total_radius, linear_velocity), pretty_round)) +
          ' rpm'
          )

    # Outer circumference of torus
    print('Outer circumference: ' +
          str(round(Formulas.circumference_of_circle(total_radius), pretty_round)) +
          ' m'
          )

    # Cross section used to calculate force acting on torus
    print('Cross Section of torus: ' +
          str(round(Formulas.cross_section_hollow_torus(outer_radius, wall_thickness), pretty_round)) +
          ' m2'.translate(superscript)
          )

    # Convert to imperial so it's easier to read
    print('Internal radius of torus: ' +
          str(round(Conversions.meter_to_feet(outer_radius - wall_thickness), pretty_round)) +
          ' ft'
          )

    # Useful when performing other calculations
    print('Angular Velocity: ' +
          str(round(Conversions.rpm_to_angular(rpm), pretty_round)) +
          ' rad/s'
          )

    # Give others an idea how big torus would be
    print('Stories high: ' +
          str(round((total_radius * Decimal(2)) / Decimal(ft_per_story))) +
          ' (' + str(ft_per_story) + ' ft per story)'.translate(superscript)
          )
    # Mass of ring
    print('Mass: ' +
          str(round(density_of_material * volume_of_walls + additional_mass, 2)) +
          ' kg'
          )

    print('---------------------')
    # Force along cross sectional area in MPa
    print('Force on torus: ' +
          str(round(stress, 2)) +
          ' MPa'
          )

    if stress <= tensile_strength:
        print("The torus can hold itself with: " + str(round(tensile_strength - stress, 2)) +
              ' MPa remaining (' + str(100 * (1 - round((tensile_strength - stress) / tensile_strength, 2)))
              + "% of total applicable)")
    else:
        print("The torus can't hold itself with: " + str(round(tensile_strength - stress, 2)) +
              ' MPa in excess (' + str(100 * (1 - round((tensile_strength - stress) / tensile_strength, 2)))
              + "% of total applicable)")

    Drawing.draw_torus(total_radius, outer_radius, kind=GraphType.MPL, z_ratio=0)


if __name__ == "__main__":
    run()
