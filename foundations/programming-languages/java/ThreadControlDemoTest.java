package kamakura.codelabs.basic_language;

import org.junit.Test;

import java.util.concurrent.locks.LockSupport;

public class ThreadControlDemoTest {
    @Test
    public void foo() throws InterruptedException {
        Object commonLock = new Object();
        ThreadControlDemo.TaskThread[] workers = new ThreadControlDemo.TaskThread[4];

        for (int i = 0; i < workers.length; i++) {
            workers[i] = new ThreadControlDemo.TaskThread(commonLock, i);
            workers[i].start();
        }

        Thread.sleep(1000); // 模拟准备阶段

        // 逐个唤醒 worker（模拟通知控制）
        for (int i = 0; i < workers.length; i++) {
            synchronized (commonLock) {
                System.out.println("主线程 notify() -> " + workers[i].getName());
                commonLock.notify(); // 唤醒一个线程
            }

            if (i == 2) {
                // 第 3 个线程我们中断
                System.out.println("主线程 interrupt() -> " + workers[i].getName());
                workers[i].interrupt();
            }

            Thread.sleep(1000);
        }

        System.out.println("主线程准备唤醒 Task-3...");
        LockSupport.unpark(workers[3]); // 唤醒 park 的线程

        // 等待所有线程结束（使用 join）
        for (ThreadControlDemo.TaskThread t : workers) {
            t.join();
        }

        System.out.println("主线程结束");
    }
}
