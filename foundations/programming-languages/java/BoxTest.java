package kamakura.codelabs.basic_language;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class BoxTest {

    @Test
    public void testBox() {
        Box<String> box = new Box<>();
        box.set("BOXER");
        System.out.println(box.get());
        assertEquals("BOXER", box.get());
    }
}
