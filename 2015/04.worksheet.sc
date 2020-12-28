def md5Hash(text: String): String = java.security.MessageDigest
  .getInstance("MD5")
  .digest(text.getBytes())
  .map(0xff & _)
  .map { "%02x".format(_) }
  .foldLeft("") { _ + _ }

val salt = "yzbqklnj"

Stream
  .from(1)
  .find(i => {
    val plain = salt + i.toString()
    val hash = md5Hash(plain)
    hash.startsWith("00000")
  })

// Stream
//   .from(282749)
//   .find(i => {
//     val plain = salt + i.toString()
//     val hash = md5Hash(plain)
//     hash.startsWith("000000")
//   })
