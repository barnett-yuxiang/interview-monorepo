package kamakura.codelabs.basic_language_v2

//fun <T> isOfType(value: Any): Boolean {
//    return value is T // Cannot check for instance of erased type
//}

inline fun <reified T> isOfType(value: Any): Boolean {
    return value is T
}
