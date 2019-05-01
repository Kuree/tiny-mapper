from tiny_mapper import *
import pytest
import os


@pytest.fixture
def design_top():
    return os.path.join(os.path.dirname(__file__),
                        "harris_design_top.json")


def test_load(design_top):
    load_src(design_top)


def test_inst_int(design_top):
    mod = load_src(design_top)
    r, _ = instance_to_int(mod)
    assert len(r) > 0


def test_get_name(design_top):
    mod = load_src(design_top)
    _, instances = instance_to_int(mod)
    for name, inst in instances.items():
        get_name(inst)


def test_get_pe_op(design_top):
    mod = load_src(design_top)
    _, instances = instance_to_int(mod)
    for name, inst in instances.items():
        namespace, name = get_name(inst)
        if namespace == "coreir":
            get_pe_operand(namespace, name)


def test_map_lb(design_top):
    c = coreir.Context()
    mod = load_src(design_top)
    _, instances = instance_to_int(mod)
    for name, inst in instances.items():
        namespace, name = get_name(inst)
        if namespace == "commonlib":
            map_common_lib(inst, c)
