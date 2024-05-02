# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cacti_interface.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='cacti_interface.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x15\x63\x61\x63ti_interface.proto\"\xdf\x08\n\nCactiInput\x12\x13\n\x0b\x63onfig_file\x18\x01 \x02(\t\x12\x33\n\ntech_param\x18\x02 \x01(\x0b\x32\x1f.CactiInput.TechnologyParameter\x12/\n\x0b\x63onst_param\x18\x03 \x01(\x0b\x32\x1a.CactiInput.ConstParameter\x12\x18\n\x10\x64yn_param_prefix\x18\x04 \x01(\t\x12\x13\n\x0bwire_config\x18\x05 \x01(\t\x1a\xdf\x06\n\x13TechnologyParameter\x12=\n\tsram_cell\x18\x01 \x01(\x0b\x32*.CactiInput.TechnologyParameter.DeviceType\x12<\n\x08\x64ram_acc\x18\x02 \x01(\x0b\x32*.CactiInput.TechnologyParameter.DeviceType\x12;\n\x07\x64ram_wl\x18\x03 \x01(\x0b\x32*.CactiInput.TechnologyParameter.DeviceType\x12?\n\x0bperi_global\x18\x04 \x01(\x0b\x32*.CactiInput.TechnologyParameter.DeviceType\x12\x44\n\nwire_local\x18\x05 \x01(\x0b\x32\x30.CactiInput.TechnologyParameter.InterconnectType\x12I\n\x0fwire_inside_mat\x18\x06 \x01(\x0b\x32\x30.CactiInput.TechnologyParameter.InterconnectType\x12J\n\x10wire_outside_mat\x18\x07 \x01(\x0b\x32\x30.CactiInput.TechnologyParameter.InterconnectType\x12\x0b\n\x03vpp\x18\x08 \x01(\x01\x12\x16\n\x0e\x64ram_cell_I_on\x18\t \x01(\x01\x12\x15\n\rdram_cell_Vdd\x18\n \x01(\x01\x12\x10\n\x08\x63\x61\x63he_sz\x18\x0b \x01(\x05\x1a\xe4\x01\n\nDeviceType\x12\x10\n\x08R_nch_on\x18\x01 \x01(\x01\x12\x10\n\x08R_pch_on\x18\x02 \x01(\x01\x12\x0b\n\x03Vdd\x18\x03 \x01(\x01\x12\x0b\n\x03Vth\x18\x04 \x01(\x01\x12\x0f\n\x07Vcc_min\x18\x05 \x01(\x01\x12\x0e\n\x06I_on_n\x18\x06 \x01(\x01\x12\x0e\n\x06I_on_p\x18\x07 \x01(\x01\x12\x0f\n\x07I_off_n\x18\x08 \x01(\x01\x12\x0f\n\x07I_off_p\x18\t \x01(\x01\x12\x10\n\x08I_g_on_n\x18\n \x01(\x01\x12\x10\n\x08I_g_on_p\x18\x0b \x01(\x01\x12!\n\x19n_to_p_eff_curr_drv_ratio\x18\x0c \x01(\x01\x1a;\n\x10InterconnectType\x12\x10\n\x08R_per_um\x18\x01 \x01(\x01\x12\x15\n\rR_per_um_mult\x18\x02 \x01(\x01\x1a\x45\n\x0e\x43onstParameter\x12\x16\n\x0e\x43U_RESISTIVITY\x18\x01 \x01(\x01\x12\x1b\n\x13\x42ULK_CU_RESISTIVITY\x18\x02 \x01(\x01'
)




_CACTIINPUT_TECHNOLOGYPARAMETER_DEVICETYPE = _descriptor.Descriptor(
  name='DeviceType',
  full_name='CactiInput.TechnologyParameter.DeviceType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='R_nch_on', full_name='CactiInput.TechnologyParameter.DeviceType.R_nch_on', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='R_pch_on', full_name='CactiInput.TechnologyParameter.DeviceType.R_pch_on', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Vdd', full_name='CactiInput.TechnologyParameter.DeviceType.Vdd', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Vth', full_name='CactiInput.TechnologyParameter.DeviceType.Vth', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Vcc_min', full_name='CactiInput.TechnologyParameter.DeviceType.Vcc_min', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='I_on_n', full_name='CactiInput.TechnologyParameter.DeviceType.I_on_n', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='I_on_p', full_name='CactiInput.TechnologyParameter.DeviceType.I_on_p', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='I_off_n', full_name='CactiInput.TechnologyParameter.DeviceType.I_off_n', index=7,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='I_off_p', full_name='CactiInput.TechnologyParameter.DeviceType.I_off_p', index=8,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='I_g_on_n', full_name='CactiInput.TechnologyParameter.DeviceType.I_g_on_n', index=9,
      number=10, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='I_g_on_p', full_name='CactiInput.TechnologyParameter.DeviceType.I_g_on_p', index=10,
      number=11, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='n_to_p_eff_curr_drv_ratio', full_name='CactiInput.TechnologyParameter.DeviceType.n_to_p_eff_curr_drv_ratio', index=11,
      number=12, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=785,
  serialized_end=1013,
)

_CACTIINPUT_TECHNOLOGYPARAMETER_INTERCONNECTTYPE = _descriptor.Descriptor(
  name='InterconnectType',
  full_name='CactiInput.TechnologyParameter.InterconnectType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='R_per_um', full_name='CactiInput.TechnologyParameter.InterconnectType.R_per_um', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='R_per_um_mult', full_name='CactiInput.TechnologyParameter.InterconnectType.R_per_um_mult', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1015,
  serialized_end=1074,
)

_CACTIINPUT_TECHNOLOGYPARAMETER = _descriptor.Descriptor(
  name='TechnologyParameter',
  full_name='CactiInput.TechnologyParameter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sram_cell', full_name='CactiInput.TechnologyParameter.sram_cell', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dram_acc', full_name='CactiInput.TechnologyParameter.dram_acc', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dram_wl', full_name='CactiInput.TechnologyParameter.dram_wl', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='peri_global', full_name='CactiInput.TechnologyParameter.peri_global', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='wire_local', full_name='CactiInput.TechnologyParameter.wire_local', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='wire_inside_mat', full_name='CactiInput.TechnologyParameter.wire_inside_mat', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='wire_outside_mat', full_name='CactiInput.TechnologyParameter.wire_outside_mat', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='vpp', full_name='CactiInput.TechnologyParameter.vpp', index=7,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dram_cell_I_on', full_name='CactiInput.TechnologyParameter.dram_cell_I_on', index=8,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dram_cell_Vdd', full_name='CactiInput.TechnologyParameter.dram_cell_Vdd', index=9,
      number=10, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cache_sz', full_name='CactiInput.TechnologyParameter.cache_sz', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_CACTIINPUT_TECHNOLOGYPARAMETER_DEVICETYPE, _CACTIINPUT_TECHNOLOGYPARAMETER_INTERCONNECTTYPE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=211,
  serialized_end=1074,
)

_CACTIINPUT_CONSTPARAMETER = _descriptor.Descriptor(
  name='ConstParameter',
  full_name='CactiInput.ConstParameter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='CU_RESISTIVITY', full_name='CactiInput.ConstParameter.CU_RESISTIVITY', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='BULK_CU_RESISTIVITY', full_name='CactiInput.ConstParameter.BULK_CU_RESISTIVITY', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1076,
  serialized_end=1145,
)

_CACTIINPUT = _descriptor.Descriptor(
  name='CactiInput',
  full_name='CactiInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='config_file', full_name='CactiInput.config_file', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tech_param', full_name='CactiInput.tech_param', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='const_param', full_name='CactiInput.const_param', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dyn_param_prefix', full_name='CactiInput.dyn_param_prefix', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='wire_config', full_name='CactiInput.wire_config', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_CACTIINPUT_TECHNOLOGYPARAMETER, _CACTIINPUT_CONSTPARAMETER, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=1145,
)

_CACTIINPUT_TECHNOLOGYPARAMETER_DEVICETYPE.containing_type = _CACTIINPUT_TECHNOLOGYPARAMETER
_CACTIINPUT_TECHNOLOGYPARAMETER_INTERCONNECTTYPE.containing_type = _CACTIINPUT_TECHNOLOGYPARAMETER
_CACTIINPUT_TECHNOLOGYPARAMETER.fields_by_name['sram_cell'].message_type = _CACTIINPUT_TECHNOLOGYPARAMETER_DEVICETYPE
_CACTIINPUT_TECHNOLOGYPARAMETER.fields_by_name['dram_acc'].message_type = _CACTIINPUT_TECHNOLOGYPARAMETER_DEVICETYPE
_CACTIINPUT_TECHNOLOGYPARAMETER.fields_by_name['dram_wl'].message_type = _CACTIINPUT_TECHNOLOGYPARAMETER_DEVICETYPE
_CACTIINPUT_TECHNOLOGYPARAMETER.fields_by_name['peri_global'].message_type = _CACTIINPUT_TECHNOLOGYPARAMETER_DEVICETYPE
_CACTIINPUT_TECHNOLOGYPARAMETER.fields_by_name['wire_local'].message_type = _CACTIINPUT_TECHNOLOGYPARAMETER_INTERCONNECTTYPE
_CACTIINPUT_TECHNOLOGYPARAMETER.fields_by_name['wire_inside_mat'].message_type = _CACTIINPUT_TECHNOLOGYPARAMETER_INTERCONNECTTYPE
_CACTIINPUT_TECHNOLOGYPARAMETER.fields_by_name['wire_outside_mat'].message_type = _CACTIINPUT_TECHNOLOGYPARAMETER_INTERCONNECTTYPE
_CACTIINPUT_TECHNOLOGYPARAMETER.containing_type = _CACTIINPUT
_CACTIINPUT_CONSTPARAMETER.containing_type = _CACTIINPUT
_CACTIINPUT.fields_by_name['tech_param'].message_type = _CACTIINPUT_TECHNOLOGYPARAMETER
_CACTIINPUT.fields_by_name['const_param'].message_type = _CACTIINPUT_CONSTPARAMETER
DESCRIPTOR.message_types_by_name['CactiInput'] = _CACTIINPUT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CactiInput = _reflection.GeneratedProtocolMessageType('CactiInput', (_message.Message,), {

  'TechnologyParameter' : _reflection.GeneratedProtocolMessageType('TechnologyParameter', (_message.Message,), {

    'DeviceType' : _reflection.GeneratedProtocolMessageType('DeviceType', (_message.Message,), {
      'DESCRIPTOR' : _CACTIINPUT_TECHNOLOGYPARAMETER_DEVICETYPE,
      '__module__' : 'cacti_interface_pb2'
      # @@protoc_insertion_point(class_scope:CactiInput.TechnologyParameter.DeviceType)
      })
    ,

    'InterconnectType' : _reflection.GeneratedProtocolMessageType('InterconnectType', (_message.Message,), {
      'DESCRIPTOR' : _CACTIINPUT_TECHNOLOGYPARAMETER_INTERCONNECTTYPE,
      '__module__' : 'cacti_interface_pb2'
      # @@protoc_insertion_point(class_scope:CactiInput.TechnologyParameter.InterconnectType)
      })
    ,
    'DESCRIPTOR' : _CACTIINPUT_TECHNOLOGYPARAMETER,
    '__module__' : 'cacti_interface_pb2'
    # @@protoc_insertion_point(class_scope:CactiInput.TechnologyParameter)
    })
  ,

  'ConstParameter' : _reflection.GeneratedProtocolMessageType('ConstParameter', (_message.Message,), {
    'DESCRIPTOR' : _CACTIINPUT_CONSTPARAMETER,
    '__module__' : 'cacti_interface_pb2'
    # @@protoc_insertion_point(class_scope:CactiInput.ConstParameter)
    })
  ,
  'DESCRIPTOR' : _CACTIINPUT,
  '__module__' : 'cacti_interface_pb2'
  # @@protoc_insertion_point(class_scope:CactiInput)
  })
_sym_db.RegisterMessage(CactiInput)
_sym_db.RegisterMessage(CactiInput.TechnologyParameter)
_sym_db.RegisterMessage(CactiInput.TechnologyParameter.DeviceType)
_sym_db.RegisterMessage(CactiInput.TechnologyParameter.InterconnectType)
_sym_db.RegisterMessage(CactiInput.ConstParameter)


# @@protoc_insertion_point(module_scope)
