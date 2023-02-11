public class zad4_5 {

    public static void main(String[] args) {

        int[] nums1 = new int[100];
        int[] nums2 = new int[100];
        int[] nums3 = new int[100];

        long startTime = System.nanoTime();
        for (int i = 0; i < 100; i++)
            nums1[i] = i * 2;

        for (int i = 0; i < 100; i++)
            nums2[i] = i * 3;

        for (int i = 0; i < 100; i++) 
            nums3[i] = (nums1[i]*nums2[i])%30;

        long stopTime = System.nanoTime();
        System.out.format("Wykonanie w Java: %d nanosekund\n", stopTime - startTime);
    }

}
