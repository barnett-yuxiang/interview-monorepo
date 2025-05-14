package kamakura.codelabs.basic_language_v2

import org.junit.Test

class InlineReifiedTest {
    @Test
    fun foo() {
        println(isOfType<String>("hello"))
        println(isOfType<Int>("hello"))
    }
}
