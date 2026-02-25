package kamakura.codelabs.basic_language_v2

import org.junit.Test

class CovariantTest {
    @Test
    fun foo() {
        val dogSource: DataSource<Dog> = DogSource()
        feedAnimal(dogSource)
    }
}
