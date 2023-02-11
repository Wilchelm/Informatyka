package com.example.foodinder_app;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.util.Pair;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Main3Activity extends AppCompatActivity {


    private Random random = new Random();
    private ImageView image;
    private TextView text;
    int pom = 0;
    String photo=null;
    String name=null;
    private RequestQueue mQueue;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main3);

        mQueue = Volley.newRequestQueue(this);

        image = (ImageView) findViewById(R.id.avatar3);
        text = (TextView) findViewById(R.id.name3);

        parseJSON();
    }


    private void parseJSON() {
        String url = Swipper.api + "/exec?action=evaluate";

        JsonObjectRequest request = new JsonObjectRequest(Request.Method.GET, url, null,
                new Response.Listener<JSONObject>() {
                    @Override
                    public void onResponse(JSONObject response) {
                        try {
                            JSONArray jarray = response.getJSONArray("item");

                            JSONObject jo = jarray.getJSONObject(0);

                            photo = jo.getString("photo");
                            name = jo.getString("name");

                            String pom = "#N/A";

                            if (photo.equals(pom)==true) {
                                Pair<String,String> agab = returnRandomFromList();
                                CardItem card = new CardItem(agab.first, agab.second);
                                image.setImageBitmap(card.getDrawable());
                                text.setText(card.getName());
                            }

                            else {
                                CardItem card = new CardItem(photo, name);
                                image.setImageBitmap(card.getDrawable());
                                text.setText(card.getName());
                            }

                            restart();

                        } catch (JSONException e) {
                            Toast.makeText(getApplicationContext(), e.toString(), Toast.LENGTH_SHORT).show();
                        }


                    }
                }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                Toast.makeText(getApplicationContext(), error.getMessage(), Toast.LENGTH_SHORT).show();
            }
        });


        mQueue.add(request);

    }

    private Pair<String, String> returnRandomFromList() {

        List<Pair<String, String>> list = new ArrayList<Pair<String, String>>();
        list.add(Pair.create("https://media-cdn.tripadvisor.com/media/photo-o/0e/50/98/36/ali-baba-doner-kebab.jpg", "kebab"));
        list.add(Pair.create("https://roadtripbus.pl/wp-content/uploads/2019/01/frytki-belgijskie-przepis.jpg", "frytki"));
        list.add(Pair.create("http://greenlife.com.pl/wp-content/uploads/2014/01/Fotolia_37798945_Subscription_Monthly_M.jpg", "paluszki rybne"));
        list.add(Pair.create("http://cdn14.beszamel.smcloud.net/t/thumbs/660/441/1/user_photos/zapiekanka-z-pieczarkami-i-serem-przepis.jpg", "zapiekanka "));
        list.add(Pair.create("https://krosno24.pl/uploads/files/1278/pizza2859233_1280.jpg", "pizza"));
        list.add(Pair.create("https://bi.im-g.pl/im/97/cf/d6/z14077847M,Hot-dog.jpg", "hot dog"));
        list.add(Pair.create("https://s3.przepisy.pl/przepisy3ii/img/variants/767x0/wrapy-z-kurczakiem-i-warzywami894020.jpg", "wrapy "));
        list.add(Pair.create("https://www.thespruceeats.com/thmb/KlbIb2jMzZnPeh5IzFvz10yDk5Y=/1813x1360/smart/filters:no_upscale()/vegetarian-bean-and-rice-burrito-recipe-3378550-9_preview-5b2417e1ff1b780037a58cda.jpeg", "buritto"));
        list.add(Pair.create("https://www.kwestiasmaku.com/sites/v123.kwestiasmaku.com/files/quesadillas_z_kurczakiem_01.jpg", "quesedilla "));
        list.add(Pair.create("https://primeburger.eu/wp-content/uploads/2018/10/2_prod_angus.jpg", "Burger"));
        list.add(Pair.create("https://s3.przepisy.pl/przepisy3ii/img/variants/357x0/klasyczne-spaghetti-bolognese-z-pomidorami.jpg", "spagetti"));
        list.add(Pair.create("http://obiading.pl/wp-content/uploads/2013/08/lasagne.jpg", "lasagne"));
        list.add(Pair.create("https://ocdn.eu/pulscms-transforms/1/cR_ktkpTURBXy82Njc1OWY5MzRmNjgwZDNkMmMwNDIzNGRjMjkxMmNkZC5qcGeTlQMAzK_NFfDNDFeTBc0DFM0BvJUH2TIvcHVsc2Ntcy9NREFfLzE0MGIxY2ZlN2YwYWM1MmVkYzAxMGQ3MDk3OGU4NGJlLnBuZwDCAA", "zapiekanka makaronowa"));
        list.add(Pair.create("https://ocdn.eu/pulscms-transforms/1/Ll1ktkpTURBXy9hOGU3YmU5MjM5MTc2NTFkZjVjNGJjZTYwZWQxMTQyNC5qcGeTlQMAzLTNFoDNDKiTBc0DFM0BvJUH2TIvcHVsc2Ntcy9NREFfLzE0MGIxY2ZlN2YwYWM1MmVkYzAxMGQ3MDk3OGU4NGJlLnBuZwDCAA", "cannelloni"));
        list.add(Pair.create("https://kobietamag.pl/wp-content/uploads/2015/11/makaron-farfalle-z-dynia-pizmowa-orzechami-i-grana-padano.jpg", "farfalle"));
        list.add(Pair.create("https://s3.przepisy.pl/przepisy3ii/img/variants/1440x1080/super-szybkie-tagliatelle-z-kurczakiem658590.jpg", "tagliatelle"));
        list.add(Pair.create("https://static.smaker.pl/photos/5/5/7/557b2c0fb2b8a9ad5d04bd81aaa17a61_367613_59ccc9e3e2f45_wm.jpg", "barszcz"));
        list.add(Pair.create("https://d3iamf8ydd24h9.cloudfront.net/pictures/articles/2018/02/39528-v-900x556.jpg", "żurek"));
        list.add(Pair.create("https://s3.przepisy.pl/przepisy3ii/img/variants/767x0/grochowka.jpg", "grochówka"));
        list.add(Pair.create("https://zakochanewzupach.pl/wp-content/uploads/2017/05/ch%C5%82odnik-z-burak%C3%B3w-1-866x597.jpg", "chłodnik"));
        list.add(Pair.create("https://s3.przepisy.pl/przepisy3ii/img/variants/767x0/zupa-pomidorowa.jpg", "zupa pomidorowa"));
        list.add(Pair.create("https://s3.przepisy.pl/przepisy3ii/img/variants/767x0/classic-chicken-soup_a423933.jpg", "rosół"));
        list.add(Pair.create("https://s3.przepisy.pl/przepisy3ii/img/variants/767x0/golabki.jpg", "gołąbki"));
        list.add(Pair.create("https://ocdn.eu/pulscms-transforms/1/KXvktkpTURBXy9jMzFlODhjYzk4YmMxNDhiODMyMzFiMzQ2ZGM2ZWI5My5qcGeTlQMAQs0ISc0EqZMFzQMUzQG8lQfZMi9wdWxzY21zL01EQV8vMTQwYjFjZmU3ZjBhYzUyZWRjMDEwZDcwOTc4ZTg0YmUucG5nAMIA", "kotlet schabowy"));
        list.add(Pair.create("https://i.wpimg.pl/O/555x385/i.wp.pl/a/f/kuchnia/58011461/-EDYSK_2-galerie_nowe-polskie_obiady-148476303.jpg", "kotlet mielony (zraz)"));
        list.add(Pair.create("https://static.gotujmy.pl/ZDJECIE_PRZEPISU_ETAP/karkowka-po-cygansku-z-lubczykiem-433571.jpg", "karkówka"));
        list.add(Pair.create("https://www.kuchniabazylii.pl/wp-content/uploads/2019/02/kurczak-w-kurkumie_przepis_1.jpg", "pierś kurczaka"));
        list.add(Pair.create("https://kuchnia-marty.pl/wp-content/uploads/2015/11/1553.900.jpg", "kopytka"));
        list.add(Pair.create("https://www.winiary.pl/image.ashx/kluski-slaskie-z-sosem-pieczeniowym.jpg?fileID=210145&width=800&height=1400&frame=False&bg=0&resize=1&crop=0&hRefill=0&vRefill=0&quality=84", "kluski śląskie"));
        list.add(Pair.create("https://kulinarneprzeboje.pl/wp-content/uploads/2018/08/DSC_0793-660x993.jpg", "knedle"));
        list.add(Pair.create("https://static.gotujmy.pl/ZDJECIE_PRZEPISU_ETAP/krokiety-z-miesem-grzybami-i-kapusta-415737.jpg", "krokiety z mięsem"));
        list.add(Pair.create("https://cookit.pl/Data/Images/zjemto.blox.pl/2015_slash_12_slash_Krokiety-z-kapusta-i-grzybami/l/-1540155321.jpg", "krokiety z kapustą i grzybami"));
        list.add(Pair.create("https://www.nalesniki.eu/wp-content/uploads/2015/02/nalesniki_z_serem.jpg", "naleśniki z serem"));
        list.add(Pair.create("https://d3iamf8ydd24h9.cloudfront.net/pictures/articles/2018/01/21290-v-900x556.jpg", "naleśniki z owocami"));
        list.add(Pair.create("https://static.gotujmy.pl/ZDJECIE_PRZEPISU_ETAP/gofry-z-bita-smietana-i-owocami-366132.jpg", "gofry z bitą śmietaną"));
        list.add(Pair.create("https://www.mniammniam.com/obrazki_mobile/sernik_latwyszybki1_mobile.jpg", "sernik"));
        list.add(Pair.create("https://www.przyslijprzepis.pl/media/cache/default_view/uploads/media/default/0001/13/2daa72a1a0a24e7dae3da924681d31e7929557a1.jpeg", "lody czekoladowe"));
        list.add(Pair.create("https://2.bp.blogspot.com/-KIAqdG_dEBc/W1CR4mRLcDI/AAAAAAAAUvA/ryRpfubKHCYe_DcRokWK1zHNm-rrJOCbQCLcBGAs/s1600/Domowe%2BLody%2B%25C5%259Bmietankowe%2Blody%2Bmleczne%2Blody%2Bsmietankowe%2Bnajlepsze%2Blody%2Bsmietankowe%2Bnajlepsze%2Blody%2B%25C5%259Bmietanowe%2Bdomowe%2Blody%2Bnajlepsze%2Bprzepis%2Bprzepis%2Bna%2Blody%2B0.jpg", "lody śmietankowe"));
        list.add(Pair.create("https://static.mojewypieki.com/upload/images/przepisy/Tiramisu/Tiramisu_01.jpg", "tiramisu"));
        list.add(Pair.create("https://s3.przepisy.pl/przepisy3ii/img/variants/767x0/wuzetka6100240536839567.jpg", "wuzetka"));
        list.add(Pair.create("http://www.przepisykulinarne.info/wp-content/uploads/2015/01/jajecznica-z-boczkiem-2.jpg", "jajecznica"));
        list.add(Pair.create("https://ocdn.eu/pulscms-transforms/1/kHcktkqTURBXy85ZTRmMmRhMWE3NGMxOWI2ZTIwMjdlYTJiNmYxMzk0Yy5qcGVnk5UDAM0Jj80NVc0HgJMFzQMUzQG8lQfZMi9wdWxzY21zL01EQV8vMTQwYjFjZmU3ZjBhYzUyZWRjMDEwZDcwOTc4ZTg0YmUucG5nAMIA", "jajecznica bez mięsa"));
        list.add(Pair.create("https://d1doqjmisr497k.cloudfront.net/-/media/kamispl-2016/recipe/2000/tosty_z_szynka_i_serem_2000.jpg?vd=20180617T003946Z&ir=1&width=885&height=498&crop=auto&quality=75&speed=0&hash=B683193C23502612DDCBE5E63A072D72C5D6A0C6", "tost"));
        list.add(Pair.create("https://i.pinimg.com/474x/31/e4/9e/31e49eadb4c89d83045b0abcc4cd187b.jpg", "tost bez miesa"));
        list.add(Pair.create("https://www.eksperymentalnie.com/wp-content/uploads/2009/01/zupa_mleczna.jpg", "zupa mleczna"));
        list.add(Pair.create("https://www.mojegotowanie.pl/media/cache/default_view/uploads/media/default/0001/06/06c1ddd737685ab33c7e9e16312264390ff37ed5.jpeg", "omlet"));
        list.add(Pair.create("https://pliki.portalspozywczy.pl/i/08/79/02/087902_940.jpg", "kanapka"));
        list.add(Pair.create("https://s3.przepisy.pl/przepisy3ii/img/variants/435x0/kanapka-z-gorgonzola-i-gruszka671748.jpg", "kanapka bez miesa"));
        list.add(Pair.create("http://jamiprzepisy.pl/wp-content/uploads/2009/05/kotlety_soczewicowe_2_1400.jpg", "kotlety z soczewicy"));
        list.add(Pair.create("https://www.przyslijprzepis.pl/media/cache/default_view/uploads/media/recipe/0006/16/c28f37349627c7dd1eb1944a1ef43c24b08ee155.jpeg", "kotlety z fasoli"));
        list.add(Pair.create("https://s3.party.pl/styl-zycia/zdrowie/odchudzanie-i-diety/zielony-wegetarianski-burger-437024-MT.jpg", "burger wege"));
        list.add(Pair.create("https://v.wpimg.pl/NzI4NDc0YRsoVjh3TEtsDmsObC0KEmJYPBZ0Zkx_YUx9ADZwWwNhHmdDPi0OV2AKJRt7fVsFeUJ8AWNpWgN9SH0Gf3BUHzkfLlUgNwhZYxg8RikhER4kCi4WMw==", "burger wege 2"));
        list.add(Pair.create("https://static.smaker.pl/photos/9/4/4/9442fbd2e845b0173b063c4ee272dccc_110705_57b497ef426c8_wm.jpg", "placki ziemniaczane"));
        list.add(Pair.create("https://s3.przepisy.pl/przepisy3ii/img/variants/767x0/2277786.jpg", "ratatuj"));
        list.add(Pair.create("http://magicznyskladnik.pl/wp-content/uploads/2015/03/przepis-na-ziemniaki-pieczone-w-piekarniku-28-2.jpg", "pieczone ziemniaki"));
        list.add(Pair.create("https://www.winiary.pl/image.ashx/losos-z-koperkiem.jpg?fileID=43312&width=800&height=1400&frame=False&bg=0&resize=1&crop=0&hRefill=0&vRefill=0&quality=84", "łosos"));
        list.add(Pair.create("http://cdn30.beszamel.smcloud.net/t/thumbs/640/480/1/user_photos/18671/tani-dorsz-z-kauflandu-najlepszy-przepis.jpg", "dorsz"));
        list.add(Pair.create("https://rybyswiata.pl/wp-content/uploads/2013/10/halibut-niebieski-rybyswiata-pl.png", "halibut"));
        list.add(Pair.create("https://www.poezja-smaku.pl/wp-content/uploads/2012/07/aromatyczny-dorsz.jpg", "dorsz w panierce"));
        list.add(Pair.create("https://media-cdn.tripadvisor.com/media/photo-s/10/19/f2/0b/ryba-miruna-w-zlocistej.jpg", "miruna w panierce"));


        int index = random.nextInt(list.size());
        return list.get(index);
    }

    private void restart(){
        String url = Swipper.api + "/exec?action=restart";

        StringRequest stringRequest = new StringRequest(Request.Method.GET, url,
                new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {
                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        Toast.makeText(getApplicationContext(), error.getMessage(), Toast.LENGTH_SHORT).show();
                    }
                });
        mQueue.add(stringRequest);
    }
}