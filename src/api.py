from .loader import DimensionLoader
from .calculator import calculate_cut_length
from .models import Connection, CutRequest

def get_cut_length(loader: DimensionLoader, type_a: str, size_a: str, type_b: str, size_b: str, c2c: float, use_g1_for_type_a: bool = False, use_g1_for_type_b: bool = False):
    """
    Returns (CutRequest, cut_length)
    
    Args:
        loader: DimensionLoader instance
        type_a: Connector type A
        size_a: Size of connector A
        type_b: Connector type B
        size_b: Size of connector B
        c2c: Center-to-center distance
        use_g1_for_type_a: If True, use G1 offset for type_a instead of normal offset
        use_g1_for_type_b: If True, use G1 offset for type_b instead of normal offset
    """
    # Get normal offsets
    offset_a = loader.get_offset(type_a, size_a)
    offset_b = loader.get_offset(type_b, size_b)
    
    # Override with G1 offsets if requested and available
    if use_g1_for_type_a:
        g1_offset_a = loader.get_offset_g1(type_a, size_a)
        if g1_offset_a is not None:
            offset_a = g1_offset_a
    
    if use_g1_for_type_b:
        g1_offset_b = loader.get_offset_g1(type_b, size_b)
        if g1_offset_b is not None:
            offset_b = g1_offset_b

    conn_a = Connection(type_a, size_a, offset_a)
    conn_b = Connection(type_b, size_b, offset_b)
    request = CutRequest(conn_a, conn_b, c2c)

    cut_length = calculate_cut_length(c2c, offset_a, offset_b)
    return request, cut_length




