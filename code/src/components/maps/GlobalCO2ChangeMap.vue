<template>

  <div class="container justify-center items-center content-center">
    <div id="globalCO2ChangeMap"></div>

    <div class="map-overlay" id="legend">
      <div class="q-pa-xm">
        <!--        <div class="text-h6">Global GHG emission, 2005-2020</div>-->
        <!--        <div class="q-gutter-sm">-->
        <!--          <q-radio-->
        <!--            v-model="emission_type"-->
        <!--            val="co2"-->
        <!--            label="CO2"-->
        <!--            color="light-green-14"-->
        <!--            v-on:click.enter="updateData"-->
        <!--          ></q-radio>-->
        <!--          <q-radio-->
        <!--            v-model="emission_type"-->
        <!--            val="ghg"-->
        <!--            label="All GHGs"-->
        <!--            color="teal"-->
        <!--            v-on:click.enter="updateData"-->
        <!--          ></q-radio>-->
        <!--        </div>-->

        <div class="q-gutter-sm">
          <q-radio
            v-model="total_or_per_cap"
            val="per_capita"
            label="Per Capita"
            color="light-green-14"
            v-on:click.enter="updateData"
          ></q-radio>
          <q-radio
            v-model="total_or_per_cap"
            val="total"
            label="Total"
            color="teal"
            v-on:click.enter="updateData"
          ></q-radio>
        </div>

      </div>

      <!--      <div>Carbon dioxide equivalents</div>-->
      <div> ({{ emission_unit }})</div>

      <div style="text-align: left" v-for="item in legend_items" :key="item">
        <span
          class="legend-key"
          v-bind:style="'background-color:' + item.color"
        ></span
        ><span>{{ item.value }}</span>
      </div>

      <q-space class="q-ma-sm"/>
      <label id="year">Year: {{ sliderValue }}</label>

      <input
        id="slider"
        type="range"
        min="2001"
        max="2020"
        step="1"
        v-model="sliderValue"
        v-on:change="updateData"
      />
    </div>
  </div>

</template>
<script>
import mapboxgl from "mapbox-gl";
import 'mapbox-gl/dist/mapbox-gl.css';

export default {
  name: "GlobalCO2ChangeMap",
  data() {
    return {
      data_dir: "data/co2_change_country_2000-2020.geojson",
      total_or_per_cap: "per_capita",  // per_capita, total
      emission_type: "co2_change",
      emission_unit: "million ton",
      map: "",
      accessToken:
        "pk.eyJ1IjoiYmluZ3hpbmtlIiwiYSI6ImNrZGg4bDNxcDF6MHEydnBlbmMyejIxZDYifQ.6WlEfCVuelKrUqOI3fhTCw",
      style_url: "mapbox://styles/bingxinke/cl4d5gdqv001514oa87j3fjxd",
      legend_items: [],
      sliderValue: "2020",
      // year: "2020",
      color_stairs: [
        "#84fab0", "#08BAAD", "#6DC6A6",
        "#9FD0A8", "#C6DBB4", "#F8DCBC",
        "#F3AE7D", "#F19563", "#EF7A4E",
      ],
      data_steps_dict: {
        "co2_change_per_capita": [-5, -3, -1.5, -0.5, 0, 0.5, 1.5, 3],
        "co2_change_total": [-250, -200, -100, -50, 0, 50, 100, 200]
      },
      unit_dict: {
        "co2_change_per_capita": "ton",
        "co2_change_total": "million ton",
      }
    };
  },
  methods: {

    updateLegend: function () {
      var data_steps = this.data_steps_dict[this.emission_type + '_' + this.total_or_per_cap]
      console.log()
      var values = [
        ` [0, ${data_steps[0]})`,
        ` [${data_steps[0]}, ${data_steps[1]})`,
        ` [${data_steps[1]}, ${data_steps[2]})`,
        ` [${data_steps[2]}, ${data_steps[3]})`,
        ` [${data_steps[3]}, ${data_steps[4]})`,
        ` [${data_steps[4]}, ${data_steps[5]})`,
        ` [${data_steps[5]}, ${data_steps[6]})`,
        ` [${data_steps[6]}, ${data_steps[7]})`,
        ` ${data_steps[7]} +`,
        " No data",
      ];
      var colors = this.color_stairs;
      colors.push("white")

      this.legend_items = [];
      for (var i = 0; i < values.length; i++) {
        var value = values[i];
        var color = colors[i];
        this.legend_items.push({value, color});
      }

      // update unit
      this.emission_unit = this.unit_dict[this.emission_type + '_' + this.total_or_per_cap]
    },

    updateData: function () { // TODO
      this.updateLegend();

      // Update data
      var data_steps = this.data_steps_dict[this.emission_type + '_' + this.total_or_per_cap]
      var color_stairs = this.color_stairs
      this.map.setPaintProperty("countries-layer", "fill-color", [
        "case",
        ["==", ["get", this.emission_type + "_" + this.total_or_per_cap + "_" + this.sliderValue], null],
        "white",
        [
          "step",
          ["get", this.emission_type + "_" + this.total_or_per_cap + "_" + this.sliderValue],
          color_stairs[0],
          data_steps[0],
          color_stairs[1],
          data_steps[1],
          color_stairs[2],
          data_steps[2],
          color_stairs[3],
          data_steps[3],
          color_stairs[4],
          data_steps[4],
          color_stairs[5],
          data_steps[5],
          color_stairs[6],
          data_steps[6],
          color_stairs[7],
          data_steps[7],
          color_stairs[8]
        ],
      ]);
    },
  },


  mounted() {
    mapboxgl.accessToken = this.accessToken;

    var bounds = [
      [-180, -60], // Southwest coordinates
      [180, 80], // Northeast coordinates
    ];

    var map = new mapboxgl.Map({
      container: "globalCO2ChangeMap",
      style: this.style_url,
      center: [0, 10],
      zoom: 1.8,
      maxBounds: bounds, // Sets bounds as max
    });

    var hoveredStateId = null;

    map.on("load", () => {
      // Add a source for the country polygons.
      map.addSource("countries", {
        type: "geojson",
        data: this.data_dir,
        generateId: true, // This ensures that all features have unique IDs
      });

      // Add a layer showing the country polygons.
      map.addLayer(
        {
          id: "countries-layer",
          type: "fill",
          source: "countries",
          paint: {},
        },
        "waterway-label"
      );
      this.updateData();


      // Create a popup, but don't add it to the map yet.
      var popup = new mapboxgl.Popup({
        closeButton: false,
        closeOnClick: false,
      });
      // Change the cursor to a pointer when the mouse is over the states layer.
      // Update popup window on hover.
      map.on("mousemove", "countries-layer", (e) => {
        map.getCanvas().style.cursor = "pointer";
        var popupInfo;

        var _type_text = this.total_or_per_cap
        if ('per_capita' === _type_text) {
          _type_text = "per capita"
        }
        var _emission_text = this.emission_type
        if ('co2' === _emission_text) {
          _emission_text = "CO<sub>2</sub>"
        } else {
          _emission_text = "GHGs"
        }
        if (
          !isNaN(e.features[0].properties[this.emission_type + "_" + this.total_or_per_cap + "_" + this.sliderValue])
        ) {
          popupInfo =
            "<strong>" + e.features[0].properties.name + "</strong> " + "<br/>" +
            _type_text + " " + _emission_text + " emission" + " in " + this.sliderValue + ":" + "<br />"
            + e.features[0].properties[this.emission_type + "_" + this.total_or_per_cap + "_" + this.sliderValue].toFixed(3)
            + " " + this.emission_unit;
        } else {
          popupInfo =
            "<strong>" + e.features[0].properties.name + "</strong>" + ": No data";
        }
        popup.setLngLat(e.lngLat).setHTML(popupInfo).addTo(map);
        if (e.features.length > 0) {
          if (hoveredStateId !== null) {
            map.setFeatureState(
              {source: "countries", id: hoveredStateId},
              {hover: false}
            );
          }
          hoveredStateId = e.features[0].id;
          map.setFeatureState(
            {source: "countries", id: hoveredStateId},
            {hover: true}
          );
        }
      });
      // Change the cursor back to a pointer and remove popup when the mouse leaves.
      map.on("mouseleave", "countries-layer", function () {
        map.getCanvas().style.cursor = "";
        popup.remove();
        if (hoveredStateId !== null) {
          map.setFeatureState(
            {source: "countries", id: hoveredStateId},
            {hover: false}
          );
        }
        hoveredStateId = null;
      });
    });

    // Disable map zoom in/out using scroll
    map.scrollZoom.disable();
    // Disable map rotation using right click + drag
    map.dragRotate.disable();
    // Disable map rotation using touch rotation gesture
    map.touchZoomRotate.disableRotation();
    // Add zoom and rotation controls to the map.
    map.addControl(new mapboxgl.NavigationControl());

    this.map = map;
  },
};
</script>

<style scoped lang="scss">


/*Container bottom left*/
.container {
  position: relative;
  width: max(1300px, 90vw);
  height: max(600px, 60vh);
  margin: 0 auto;
}

#globalCO2ChangeMap {
  //   position: absolute;
  width: 100%;
  //width: 1300px;
  height: 100%;
}

.map-overlay {
  position: absolute;
  bottom: 5px;
  left: 5px;
  background: rgba(255, 255, 255, 0.8);
  font-family: Arial, sans-serif;
  overflow: auto;
  border-radius: 3px;
  overflow-y: hidden;
}

#legend {
  padding: 10px;
  //   padding-left: 20px;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
  line-height: 20px;
  height: 350px;
  //margin-bottom: 0px;
  width: 250px;
}

.legend-key {
  display: inline-block;
  border-radius: 20%;
  width: 10px;
  height: 10px;
  margin-left: 20px;
  //   padding-left: 20px;
}

.map-overlay input {
  background-color: transparent;
  display: inline-block;
  width: 100%;
  position: relative;
  margin: 0;
  cursor: ew-resize;
}
</style>
