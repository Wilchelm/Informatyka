using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.ServiceModel;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using WEB_SERWIS_PISY.ServiceReference1;

namespace WEB_SERWIS_PISY
{
    public partial class formWeather : Form
    {
        public formWeather()
        {
            InitializeComponent();
            BasicHttpBinding binding = new BasicHttpBinding();
            binding.MaxReceivedMessageSize = 2000000;

            EndpointAddress address = new EndpointAddress("http://www.webservicex.net/globalweather.asmx");

            GlobalWeatherSoapClient gwsc = new GlobalWeatherSoapClient(binding, address);

            var cities = gwsc.GetCitiesByCountry("");

        }
    }
}
