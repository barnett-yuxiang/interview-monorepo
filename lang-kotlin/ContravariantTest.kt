package kamakura.codelabs.basic_language_v2

import org.junit.Test

class ContravariantTest {
    @Test
    fun foo() {
        val animalConsumer : DataConsumer<Animal> = AnimalConsumer()
        feedCat(animalConsumer)
    }
}
