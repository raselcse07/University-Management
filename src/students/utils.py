import random
import string


def TrxID_generator(size=6,chars=string.digits+string.ascii_lowercase):

    return "".join(random.choice(chars) for _ in range(size))


def create_TrxID(instance,size=6):

    new_TrxID=TrxID_generator(size=size)

    klass=instance.__class__

    qs_exists=klass.objects.filter(TrxID=new_TrxID).exists()

    if qs_exists:

        return TrxID_generator(size=size)
    return new_TrxID

