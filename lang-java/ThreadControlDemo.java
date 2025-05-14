package kamakura.codelabs.basic_language;

import java.util.concurrent.locks.LockSupport;

public class ThreadControlDemo {
    static class TaskThread extends Thread {
        private final Object lock;
        private final int id;

        public TaskThread(Object lock, int id) {
            this.lock = lock;
            this.id = id;
            setName("Task-" + id);
        }

        @Override
        public void run() {
            synchronized (lock) {
                try {
                    System.out.println(getName() + " 等待启动信号...");
                    lock.wait(); // 等待主线程唤醒
                } catch (InterruptedException e) {
                    System.out.println(getName() + " 被中断，提前退出！");
                    return;
                }
            }

            // 被唤醒后开始执行
            System.out.println(getName() + " 开始执行任务...");
            for (int i = 0; i < 3; i++) {
                System.out.println(getName() + " 执行步骤 " + i);
                Thread.yield(); // 主动让出 CPU
            }

            // 如果是最后一个任务线程，则进入 LockSupport 等待
            if (id == 3) {
                System.out.println(getName() + " 使用 LockSupport.park() 进入挂起...");
                LockSupport.park();
                System.out.println(getName() + " 被 unpark() 唤醒，继续执行");
            }

            System.out.println(getName() + " 执行完毕");
        }
    }
}
