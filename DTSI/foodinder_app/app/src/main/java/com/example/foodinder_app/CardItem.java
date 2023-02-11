package com.example.foodinder_app;

import android.graphics.Bitmap;
import android.util.Log;

import com.squareup.picasso.Picasso;

public class CardItem {

    private static final String TAG = Main2Activity.class.getName();
    private final static int AVATAR_WIDTH = 1000;
    private final static int AVATAR_HEIGHT = 1000;
    private Bitmap drawable;
    private String name;
    Bitmap bitmap = null;

    public CardItem(String drawableId, String name) {
        this.drawable = setBitmapFromURL(drawableId, AVATAR_WIDTH, AVATAR_HEIGHT);
        this.name = name;
    }

    public CardItem() {}

    public Bitmap getDrawable() {
        return drawable;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void changeBitmap(Bitmap x) { bitmap = x; }

    public Bitmap setBitmapFromURL (final String src, int reqWidth, int reqHeight) {


        Thread thread = new Thread(new Runnable() {
            public void run() {
                // a potentially time consuming task
                try {
                    Bitmap y = Picasso.get().load(src).get();
                    changeBitmap(y);
                } catch (Exception e) {
                    Log.e(TAG, ""+e);
                }
            }
        });

        thread.start();

        Bitmap end = null;


        int a =0;
        while (end==null) {
            a+=1;
            try {
                end = Bitmap.createScaledBitmap(bitmap, reqWidth, reqHeight, false);
            } catch (Exception e) {

            }
        }

        bitmap = null;

        return end;

    }
}
