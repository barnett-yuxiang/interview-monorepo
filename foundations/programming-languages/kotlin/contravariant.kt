package kamakura.codelabs.basic_language_v2

interface DataConsumer<in T> {
    fun consume(data: T)
}

class Cat : Animal() {
    override fun eat() = println("Cat eats")
}

class AnimalConsumer : DataConsumer<Animal> {
    override fun consume(data: Animal) {
        data.eat()
    }
}

fun feedCat(consumer: DataConsumer<Cat>) {
    consumer.consume(Cat())
}
