# Elastic-Collision-Simulation

Consider the situation where we have two masses, one of which is larger than the other, with a fixed wall to the left of both the masses, and infinite space to the right. Both of these masses situated on a frictionless plane and undergo elastic collisions. The simulation shows, that given that these both these objects have a mass, of which is a power of 10, the number of collisions is the first n digits of pi.

![Example](example.png)

DISCLAIMER: THIS DOES NOT WORK FOR ANY PAIR OF MASSES.

## Installation and usage

```
git clone https://github.com/elliottcoops/Elastic-Collision-Simulation.git
cd Logic-Gate-Perceptron
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 main.py
```

## How does it work?

### What is an elastic collision

An elastic collision is where both momentum and kinetic energy are both conserved. This is such that, the total kinetic energy and momentum in the system of masses before, is exactly equal to that after. 

### Conservation of momentum

In any situation for momentum: P (Momentum) = M (Mass) * V (Velocity)

Thus for an elastic collision between two objects: 

  - P_before_collsion = (m1 * v1_inital) + (m2 * v2_initial)
  - P_after_collision = (m1 * v1_final) + (m2 * v2_final)

Setting these equal to one another due to an elastic collision:

  - (m1 * v1_inital) + (m2 * v2_initial) = (m1 * v1_final) + (m2 * v2_final)

### Conservation of kinetic energy

In any situation for momentum: Ek (Kinetic energy) = 0.5 * M (Mass) * V^2 (Velocity squared)

Thus for an elastic collision between two objects: 

  - Ek_before_collsion = (0.5 * m1 * v1_inital ^ 2) + (0.5 * m2 * v2_initial ^ 2)
  - Ek_after_collision = (0.5 * m1 * v1_final ^ 2) + (0.5 * m2 * v2_final ^ 2))

Setting these equal to one another due to an elastic collision:

  - (0.5 * m1 * v1_inital ^ 2) + (0.5 * m2 * v2_initial ^ 2) = (0.5 * m1 * v1_final ^ 2) + (0.5 * m2 * v2_final ^ 2)

### Why use this?

By using the equations above, we can go through a long rearranging process to attain the final equation: 

  - v1_final = (m_1 * v_1_initial - m_2 * v_1_initial + 2 * m_2 * v_2_initial) / (m_1 + m_2)

Which allows us to find the velocity of which mass one moves off at, after colliding with mass two. From this, it is also possible to find the velocity of mass two.

