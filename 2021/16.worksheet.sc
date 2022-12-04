import scala.io.Source

object Numbers {
  def leftPad(l: Int, s: String, c: Char = '0'): String =
    List.fill(l - s.length)(c).mkString + s
  def hex2bin(hex: Char): String =
      val bin = Integer.parseInt(hex.toString, 16).toBinaryString
      leftPad(4, bin)
  def hex2bin(hex: String) : String =  hex.flatMap(hex2bin(_))
  def bin2dec(bin: String) : Long = BigInt(bin, 2).longValue
}

import Numbers._

trait Packet {
    val version: Long
    val size: Long
    val versionSum : Long
    val value: Long
}
case class Literal(version: Long, size: Long, value: Long) extends Packet {
    val versionSum = version
}
case class Operator(version: Long, size: Long, typeId: Long, packets: List[Packet]) extends Packet {
    val versionSum = version + packets.map(_.versionSum).sum
    val value = typeId match {
        case 0 => packets.map(_.value).sum
        case 1 => packets.map(_.value).product
        case 2 => packets.map(_.value).min
        case 3 => packets.map(_.value).max
        case 5 => {packets match {case (a :: b :: _) => if a.value > b.value then 1 else 0 case _ => 0}}
        case 6 => {packets match {case (a :: b :: _) => if a.value < b.value then 1 else 0 case _ => 0}}
        case 7 => {packets match {case (a :: b :: _) => if a.value == b.value then 1 else 0 case _ => 0}}
        case _ => 0L
    }
}


def parseLiteral(packet: String, version: Long) : Literal = 
    val (grOne, grZero) = packet.drop(6).grouped(5).toList.span(_.head == '1')
    val size = 6 + (grOne.size + 1) * 5
    val value = bin2dec((grOne :+ grZero.head).map(_.tail).mkString)
    Literal(version, size, value)

def parseSubPackets(packet: String)(offset: Int, subPackets: List[Packet]) : (Int, List[Packet]) =
    val rem = packet.drop(offset)
    val subPacket = parse(rem)
    val newOffset = offset + subPacket.size.toInt
    (newOffset, subPackets :+ subPacket)

def parseOperator(packet: String, version: Long, packetType: Long) : Operator =
    val lengthTypeId = bin2dec(packet.drop(6).take(1))
    val fnSub = parseSubPackets(packet).tupled
    lengthTypeId match 
        case 0L => 
            val size = bin2dec(packet.drop(7).take(15)) + 22
            val init = (22, List(): List[Packet])
            val sp = Iterator
                .iterate(init)(fnSub)
                .dropWhile(_._1 < size)
                .next()
            Operator(version, size, packetType, sp._2)
        case 1L =>
            val count = bin2dec(packet.drop(7).take(11)).toInt
            val init = (18, List(): List[Packet])
            val sp = Iterator
                .iterate(init)(fnSub)
                .drop(count)
                .next()
            val size = 18 + sp._2.map(_.size).sum
            Operator(version, size, packetType, sp._2)

def parse(packet: String) : Packet =     
    val version = bin2dec(packet.take(3))
    val packetType = bin2dec(packet.drop(3).take(3))
    packetType match
        case 4 => parseLiteral(packet, version)
        case _ => parseOperator(packet, version, packetType)


var fileName = "2021/16.txt"
var input =
  Source
    .fromFile(fileName)
    .getLines()
    .mkString


val packet = parse(hex2bin(input))
val part1 = packet.versionSum
val part2 = packet.value


// 001 110 0 000000000011011 1101000101001010010001001000000000
//  V1  T6 I             L27

//      110 100 01010 01010010001001000000000
//       V6  T4    10 L=11 Remaining = 16

//      010 100 10001 00100 0000000
//       V2  T4          20 L=16 Remaining = 0