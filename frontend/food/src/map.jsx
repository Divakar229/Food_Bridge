import React from "react";
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import L from "leaflet";
import "leaflet/dist/leaflet.css";

// 1. Fix icon URLs explicitly
import markerIcon from "leaflet/dist/images/marker-icon.png";
import markerShadow from "leaflet/dist/images/marker-shadow.png";

let DefaultIcon = L.icon({
  iconUrl: markerIcon,
  shadowUrl: markerShadow,
  iconSize: [25, 41],
  iconAnchor: [12, 41],
});
L.Marker.prototype.options.icon = DefaultIcon;

const indiaBounds = [
  [6.4626999, 68.1097],
  [35.513327, 97.395358]
];

function HungerMap() {
  return (
    <div style={{ height: "100vh", width: "100vw" }}>
      <MapContainer
        center={[20.5937, 78.9629]}
        zoom={5}
        minZoom={5}
        maxBounds={indiaBounds}
        maxBoundsViscosity={1.0}
        style={{ height: "100%", width: "100%" }} // Fill the wrapper
      >
        <TileLayer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        />

        <Marker position={[15.5937, 78.9629]}>
          <Popup>Welcome to the India Hunger Map!</Popup>
        </Marker>
      </MapContainer>
    </div>
  );
}

export default HungerMap;