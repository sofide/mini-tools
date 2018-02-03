from PIL import Image

from targeter_to_test import Targeter


picture = Image.open('/home/sofi/Pictures/hermanos.jpg')
targeter = Targeter(picture)


def test_add_target():
    targets_before = len(targeter.targets)
    targeter.add_target()
    assert len(targeter.targets) == targets_before + 1


def test_add_at_last():
    targets_before = targeter.targets.copy()
    targeter.add_target()
    assert targets_before == targeter.targets[:-1]


def test_remove_target():
    targets_before = len(targeter.targets)
    targeter.remove_target()
    assert len(targeter.targets) == targets_before - 1


def test_remove_last_one():
    targets_before = targeter.targets.copy()
    targeter.remove_target()
    assert targets_before[:-1] == targeter.targets
