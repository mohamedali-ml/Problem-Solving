from typing import List  # Import List for type hinting

class Solution:  
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:  
        res = []  # Initialize an empty list to store surviving asteroids

        for a in asteroids:  # Iterate through each asteroid in the list
            while res and a < 0 < res[-1]:  # Check for a collision (right-moving asteroid meets left-moving asteroid)
                if -a > res[-1]:  # If the current asteroid (negative) is larger in magnitude
                    res.pop()  # Destroy the last asteroid in the list
                    continue  # Continue checking for further collisions
                elif -a == res[-1]:  # If both asteroids are of equal size
                    res.pop()  # Both asteroids explode
                break  # Stop checking as either collision is resolved or asteroid is destroyed
            
            else:  # If no collision occurs, add the asteroid to the list
                res.append(a)

        return res  # Return the final state of asteroids after all collisions
