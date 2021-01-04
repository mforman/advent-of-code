import scala.io.Source

sealed trait Gate
case class Variable(name: String) extends Gate
case class Const(value: Int) extends Gate
case class AndGate(left: Gate, right: Gate) extends Gate
case class OrGate(left: Gate, right: Gate) extends Gate
case class NotGate(gate: Gate) extends Gate
case class LeftShiftGate(gate: Gate, offset: Int) extends Gate
case class RightShiftGate(gate: Gate, offset: Int) extends Gate

def ConstOrVariable(in: String): Gate = {
  in match {
    case i if i.matches("\\d+") => Const(i.toInt)
    case _                      => Variable(in)
  }
}

val SignalEx = """(\w+) -> (\w+)""".r
val AndEx = """(\w+) AND (\w+) -> (\w+)""".r
val OrEx = """(\w+) OR (\w+) -> (\w+)""".r
val NotEx = """NOT (\w+) -> (\w+)""".r
val LShiftEx = """(\w+) LSHIFT (\d+) -> (\w+)""".r
val RShiftEx = """(\w+) RSHIFT (\d+) -> (\w+)""".r

// val input = """123 -> x
// 456 -> y
// x AND y -> d
// x OR y -> e
// x LSHIFT 2 -> f
// y RSHIFT 2 -> g
// NOT x -> h
// NOT y -> i""".split("\n")

val input = Source.fromFile("2015/07.txt").getLines()

def getValue(wires: Map[String, Gate], x: Gate): Int = {
  val mutableWires = scala.collection.mutable.Map() ++ wires

  def eval(gate: Gate): Int = {
    gate match {
      case Const(i) => i
      case Variable(g) => {
        val value = eval(mutableWires(g))
        mutableWires(g) = Const(value)
        value
      }
      case NotGate(g)                => (-1 * eval(g)) - 1
      case AndGate(l, r)             => eval(l) & eval(r)
      case OrGate(l, r)              => eval(l) | eval(r)
      case LeftShiftGate(g, offset)  => (eval(g) << offset) & 0xffff
      case RightShiftGate(g, offset) => eval(g) >> offset
    }
  }

  eval(x)
}

val instructions = input
  .map(s => {
    s match {
      case SignalEx(value, dest) => dest -> ConstOrVariable(value)
      case AndEx(left, right, dest) =>
        dest -> AndGate(ConstOrVariable(left), ConstOrVariable(right))
      case OrEx(left, right, dest) =>
        dest -> OrGate(ConstOrVariable(left), ConstOrVariable(right))
      case NotEx(gate, dest) => dest -> NotGate(ConstOrVariable(gate))
      case LShiftEx(gate, offset, dest) =>
        dest -> LeftShiftGate(ConstOrVariable(gate), offset.toInt)
      case RShiftEx(gate, offset, dest) =>
        dest -> RightShiftGate(ConstOrVariable(gate), offset.toInt)
    }
  })
  .toMap

val wireA = getValue(instructions, Variable("a"))

val newInstructions = instructions.updated("b", Const(wireA))
val newA = getValue(newInstructions, Variable("a"))
