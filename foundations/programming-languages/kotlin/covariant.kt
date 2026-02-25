package kamakura.codelabs.basic_language_v2

interface DataSource<out T> {
    fun getData(): T
}

open class Animal {
    open fun eat() = println("Animal2 eats")
}

class Dog : Animal()

class DogSource : DataSource<Dog> {
    override fun getData(): Dog {
        return Dog()
    }
}

fun feedAnimal(source: DataSource<Animal>) {
    val animal = source.getData()
    println("Feeding ${animal::class.simpleName}")
}
