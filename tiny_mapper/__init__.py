import coreir
import igraph
from dataclasses import dataclass
import enum
from typing import Dict


@enum.unique
class OpType(enum.Enum):
    BYPASS = enum.auto()
    VALID = enum.auto()
    CONST = enum.auto()


@dataclass
class PEOp:
    name: str
    data0_mode: OpType
    data0_reg: int
    data1_mode: OpType
    data1_reg: int
    bit0_mode: OpType
    bit0_reg: int
    bit1_mode: OpType
    bit1_reg: int
    bit2_mode: OpType
    bit2_reg: int


def load_src(src_filename, context: coreir.Context = None):
    if context is None:
        context = coreir.Context()
    context.load_library("commonlib")
    return context.load_from_file(src_filename)


def instance_to_int(mod: coreir.module.Module):
    top_def = mod.definition
    result = {}
    instances = {}

    for instance in top_def.instances:
        instance_name = instance.name
        assert instance_name not in result
        result[instance_name] = len(result)
        instances[instance_name] = instance
    return result, instances


def get_name(instance: coreir.module.Instance):
    mod = instance.module
    namespace, name = mod.namespace.name, mod.name
    assert namespace in ("coreir", "corebit", "commonlib")
    return namespace, name


def get_pe_operand(namespace: str, name: str):
    if namespace != "coreir":
        return None
    return PEOp(name, OpType.BYPASS, 0, OpType.BYPASS, 0,
                OpType.BYPASS, 0, OpType.BYPASS,
                0, OpType.BYPASS, 0)


def map_common_lib(instance: coreir.module.Instance, context: coreir.Context):
    namespace, name = get_name(instance)
    assert namespace == "commonlib"
    if name == "linebuffer":
        # need to create a bunch of registers and row buffers
        # get row size
        p = instance.module.generator_args["image_type"]




def construct_graph(mod: coreir.module.Module,
                    instance_to_id: Dict[str, int]):
    pass