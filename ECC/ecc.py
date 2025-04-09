import random



#a point on the elliptic curve

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return str(self.x) + ' - ' + str(self.y)


class EllipticCurveCryptography:

    def __init__(self, a, b):
        #y^2 = x^3 + ax +b
        # bitcoin - a=0 and b=7 (y^2 = x^3 + 7)
        self.a = a
        self.b = b



    def point_addition(self, P, Q):

        x1 ,y1 = P.x, P.y
        x2, y2 = Q.x, Q.y

        # sometimes we have to make a point addition
        # sometimes a point doubling (P=Q)

        if x1 == x2 and y1 == y2:
            # point doubling operation (P=Q)

            m = (3*x1*x1+self.a) / (2*y1)

        else:
            # point addition operation (P!=Q)
             m = (y2-y1) / (x2-x1)

        # we have to update x3 and y3 coordinates

        x3 = m*m - x1 - x2
        y3 = m*(x1-x3) - y1

        return Point(x3, y3)


            # it has 0(m) linear running time complexity
    def double_and_add(self, n, P):

        temp_point = Point(P.x, P.y)
        binary = bin(n)[3:]


        for binary_char in binary:

            # point doubling
            temp_point = self.point_addition(temp_point, temp_point)

            if binary_char == '1':
                # point addition operation
                temp_point = self.point_addition(temp_point, P)

        return temp_point



if __name__ == '__main__':

        ecc = EllipticCurveCryptography(0,7)
            # the E elliptic curve + the G generator is public
        generator_point = Point(-2, -1)

            # alice random number a
        alice_random = random.randint(2, 1e4)
        # bob random number b
        bob_random = random.randint(2, 1e4)

        # public key double and add algo
        # these are points on the elliptic curve
        alice_public = ecc.double_and_add(alice_random, generator_point)
        bob_public = ecc.double_and_add(bob_random, generator_point)

        # they can generate the private key (which will be the same)
        alice_secret_key = ecc.double_and_add(alice_random, bob_public)
        bob_secret_key = ecc.double_and_add(bob_random, alice_public)



       # p = Point(1,1)
#        print(ecc.point_addition(p, p))
       # print(ecc.double_and_add(100, p))






































