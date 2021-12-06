from binaryninja import Architecture, Type
from enum import IntEnum


class VMTOffsets(object):
    def __init__(self, delphi_version: int, ptr_size: int):
        if delphi_version == 2:
            self.cVmtSelfPtr = -(ptr_size * 13)
            self.cVmtInitTable = -(ptr_size * 12)
            self.cVmtTypeInfo = -(ptr_size * 11)
            self.cVmtFieldTable = -(ptr_size * 10)
            self.cVmtMethodTable = -(ptr_size * 9)
            self.cVmtDynamicTable = -(ptr_size * 8)
            self.cVmtClassName = -(ptr_size * 7)
            self.cVmtInstanceSize = -(ptr_size * 6)
            self.cVmtParent = -(ptr_size * 5)
            self.cVmtDefaultHandler = -(ptr_size * 4)
            self.cVmtNewInstance = -(ptr_size * 3)
            self.cVmtFreeInstance = -(ptr_size * 2)
            self.cVmtDestroy = -(ptr_size * 1)
        elif delphi_version == 3:
            self.cVmtSelfPtr = -(ptr_size * 16)
            self.cVmtIntfTable = -(ptr_size * 15)
            self.cVmtAutoTable = -(ptr_size * 14)
            self.cVmtInitTable = -(ptr_size * 13)
            self.cVmtTypeInfo = -(ptr_size * 12)
            self.cVmtFieldTable = -(ptr_size * 11)
            self.cVmtMethodTable = -(ptr_size * 10)
            self.cVmtDynamicTable = -(ptr_size * 9)
            self.cVmtClassName = -(ptr_size * 8)
            self.cVmtInstanceSize = -(ptr_size * 7)
            self.cVmtParent = -(ptr_size * 6)
            self.cVmtSafeCallException = -(ptr_size * 5)
            self.cVmtDefaultHandler = -(ptr_size * 4)
            self.cVmtNewInstance = -(ptr_size * 3)
            self.cVmtFreeInstance = -(ptr_size * 2)
            self.cVmtDestroy = -(ptr_size * 1)
        elif delphi_version in [4, 5, 6, 7, 2005, 2006, 2007]:
            self.cVmtSelfPtr = -(ptr_size * 19)
            self.cVmtIntfTable = -(ptr_size * 18)
            self.cVmtAutoTable = -(ptr_size * 17)
            self.cVmtInitTable = -(ptr_size * 16)
            self.cVmtTypeInfo = -(ptr_size * 15)
            self.cVmtFieldTable = -(ptr_size * 14)
            self.cVmtMethodTable = -(ptr_size * 13)
            self.cVmtDynamicTable = -(ptr_size * 12)
            self.cVmtClassName = -(ptr_size * 11)
            self.cVmtInstanceSize = -(ptr_size * 10)
            self.cVmtParent = -(ptr_size * 9)
            self.cVmtSafeCallException = -(ptr_size * 8)
            self.cVmtAfterConstruction = -(ptr_size * 7)
            self.cVmtBeforeDestruction = -(ptr_size * 6)
            self.cVmtDispatch = -(ptr_size * 5)
            self.cVmtDefaultHandler = -(ptr_size * 4)
            self.cVmtNewInstance = -(ptr_size * 3)
            self.cVmtFreeInstance = -(ptr_size * 2)
            self.cVmtDestroy = -(ptr_size * 1)
        elif delphi_version in [2009, 2010]:
            self.cVmtSelfPtr = -(ptr_size * 22)
            self.cVmtIntfTable = -(ptr_size * 21)
            self.cVmtAutoTable = -(ptr_size * 20)
            self.cVmtInitTable = -(ptr_size * 19)
            self.cVmtTypeInfo = -(ptr_size * 18)
            self.cVmtFieldTable = -(ptr_size * 17)
            self.cVmtMethodTable = -(ptr_size * 16)
            self.cVmtDynamicTable = -(ptr_size * 15)
            self.cVmtClassName = -(ptr_size * 14)
            self.cVmtInstanceSize = -(ptr_size * 13)
            self.cVmtParent = -(ptr_size * 12)
            self.cVmtEquals = -(ptr_size * 11)
            self.cVmtGetHashCode = -(ptr_size * 10)
            self.cVmtToString = -(ptr_size * 9)
            self.cVmtSafeCallException = -(ptr_size * 8)
            self.cVmtAfterConstruction = -(ptr_size * 7)
            self.cVmtBeforeDestruction = -(ptr_size * 6)
            self.cVmtDispatch = -(ptr_size * 5)
            self.cVmtDefaultHandler = -(ptr_size * 4)
            self.cVmtNewInstance = -(ptr_size * 3)
            self.cVmtFreeInstance = -(ptr_size * 2)
            self.cVmtDestroy = -(ptr_size * 1)
        elif delphi_version in [2011, 2012, 2013, 2014]:
            self.cVmtSelfPtr = -(ptr_size * 22)
            self.cVmtIntfTable = -(ptr_size * 21)
            self.cVmtAutoTable = -(ptr_size * 20)
            self.cVmtInitTable = -(ptr_size * 19)
            self.cVmtTypeInfo = -(ptr_size * 18)
            self.cVmtFieldTable = -(ptr_size * 17)
            self.cVmtMethodTable = -(ptr_size * 16)
            self.cVmtDynamicTable = -(ptr_size * 15)
            self.cVmtClassName = -(ptr_size * 14)
            self.cVmtInstanceSize = -(ptr_size * 13)
            self.cVmtParent = -(ptr_size * 12)
            self.cVmtEquals = -(ptr_size * 11)
            self.cVmtGetHashCode = -(ptr_size * 10)
            self.cVmtToString = -(ptr_size * 9)
            self.cVmtSafeCallException = -(ptr_size * 8)
            self.cVmtAfterConstruction = -(ptr_size * 7)
            self.cVmtBeforeDestruction = -(ptr_size * 6)
            self.cVmtDispatch = -(ptr_size * 5)
            self.cVmtDefaultHandler = -(ptr_size * 4)
            self.cVmtNewInstance = -(ptr_size * 3)
            self.cVmtFreeInstance = -(ptr_size * 2)
            self.cVmtDestroy = -(ptr_size * 1)
            # self.cVmtQueryInterface = 0
            # self.cVmtAddRef = (ptr_size * 1)
            # self.cVmtRelease = (ptr_size * 2)
            # self.cVmtCreateObject = (ptr_size * 3)
        else:
            raise RuntimeError(f'Unsuported Delphi version {delphi_version}')


class VMTFieldTypes(object):
    def __init__(self, arch: Architecture):
        self.cVmtSelfPtr = Type.pointer(arch, Type.void())
        self.cVmtIntfTable = Type.pointer(arch, Type.void())
        self.cVmtAutoTable = Type.pointer(arch, Type.void())
        self.cVmtInitTable = Type.pointer(arch, Type.void())
        self.cVmtTypeInfo = Type.pointer(arch, Type.void())
        self.cVmtFieldTable = Type.pointer(arch, Type.void())
        self.cVmtMethodTable = Type.pointer(arch, Type.void())
        self.cVmtDynamicTable = Type.pointer(arch, Type.void())
        self.cVmtClassName = Type.pointer(arch, Type.void())
        self.cVmtInstanceSize = Type.int(arch.address_size)
        self.cVmtParent = Type.pointer(arch, Type.void())