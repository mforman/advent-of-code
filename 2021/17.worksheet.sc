
import scala.io.Source

case class Point(x: Int, y: Int) {
  def +(p: Point): Point = Point(x + p.x, y + p.y)
}

case class Probe(p: Point, v:Point) {
  def move(): Probe = 
    val vx = v.x match
      case _ if v.x < 0 => v.x + 1
      case _ if v.x == 0 => 0
      case _ => v.x - 1
    
    Probe(p+v, Point(vx, v.y-1))
}

case class Target(topLeft:Point, bottomRight:Point) {
  def inTarget(p: Point) = p.x >= topLeft.x && p.x <= bottomRight.x && p.y<= topLeft.y && p.y >= bottomRight.y
  def overshot(p: Point) = p.x > bottomRight.x || p.y < bottomRight.y
  def inFlight(p: Point) = !inTarget(p) && !overshot(p)
}

def parse(s: String) : Target =
  val regex = """.*x=(\d+)..(\d+), y=(-?\d+)..(-?\d+)""".r
  s match 
    case regex(x1, x2, y2, y1) => Target(Point(x1.toInt, y1.toInt), Point(x2.toInt, y2.toInt))
  
var fileName = "2021/17a.txt"
var input =
  Source
    .fromFile(fileName)
    .getLines()
    .mkString

val target = parse(input)
val start = Point(0,0)
val probe = Probe(Point(0,0), Point(7,2))

(1 to target.bottomRight.x).flatMap(x => (target.bottomRight.y to -target.bottomRight.y).map(y => Probe(start, Point(x,y))))

