from manim import *

class Particle:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

class Spring:
    def __init__(self, k, particle1, particle2):
        self.k = k
        self.particle1 = particle1
        self.particle2 = particle2

    def calculate_force(self):
        distance = self.particle1.position - self.particle2.position
        force = -self.k * distance
        return force

class MassSpringSystemAnimation(Scene):
    def construct(self):
        # Create the particles and spring
        particle1 = Particle(np.array([0, 0]), np.array([0, 0]))
        particle2 = Particle(np.array([1, 0]), np.array([0, 0]))
        spring = Spring(10, particle1, particle2)

        # Add the particles and spring to the scene
        self.add(particle1)
        self.add(particle2)
        self.add(spring)

        # Animate the system
        for i in range(100):
            # Calculate the force on each particle
            force1 = spring.calculate_force()
            force2 = -force1

            # Update the particles' velocities
            particle1.velocity += force1 / particle1.mass
            particle2.velocity += force2 / particle2.mass

            # Update the particles' positions
            particle1.position += particle1.velocity
            particle2.position += particle2.velocity

            # Update the spring
            spring.update()

            # Update the scene
            self.update()

        # Wait for a few seconds before ending the animation
        self.wait(2)

class MassSpringSystemAnimation(Scene):
    def construct(self):
        # Create the particles and spring
        particle1 = Particle(np.array([0, 0]), np.array([0, 0]))
        particle2 = Particle(np.array([1, 0]), np.array([0, 0]))
        spring = Spring(10, particle1, particle2)

        # Add the particles and spring to the scene
        self.add(particle1)
        self.add(particle2)
        self.add(spring)

        # Create a vector field to represent the force on each particle
        vector_field = VectorField(lambda x: spring.calculate_force(x))

        # Add the vector field to the scene
        self.add(vector_field)

        # Animate the system
        for i in range(100):
            # Update the particles' velocities and positions
            particle1.update()
            particle2.update()

            # Update the spring
            spring.update()

            # Update the vector field
            vector_field.update()

            # Update the scene
            self.update()

        # Wait for a few seconds before ending the animation
        self.wait(2)
