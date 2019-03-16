import z3

def string_to_z3expression(smt2_string):
  """
  Parses a string to a z3expression

  As STLInspector uses only smt2 strings with one assert, it is save to take the first element.

  Args:
    smt2_string : The string, which should be converted
  
  Returns:
    The ast of the first assert in smt2_string
  """
  parsedAsserts = list(z3.parse_smt2_string(smt2_string))
  assert len(parsedAsserts) == 1
  return parsedAsserts[0]
