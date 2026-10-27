package comp.agrega;

import java.util.ArrayList;

public class Laptop {
    private String modelo;
    private int cantApp;
    private ArrayList<Aplicacion> apps = new ArrayList<>();
    private Pantalla pantalla; // COMPOSICION

    public Laptop(String modelo, int cantApp, String tipo, int ancho, int alto) {
        this.modelo = modelo;
        this.cantApp = cantApp;
        this.pantalla = new Pantalla(tipo, ancho, alto); 
    }

    // AGREGACION
    public void agregaApp(Aplicacion app){
        if(apps.size() < 50){
            this.apps.add(app);
            this.cantApp = apps.size();
        }
    }
    
    // inciso d
    public void eliminarApps(){
        this.apps.clear();
        this.cantApp = 0;
    }
    
    // inciso f - ordenar decreciente por tamanio, si empata por nombre
    public void ordenarApps(){
        apps.sort((a1, a2) -> {
            if(a2.getTamanio() != a1.getTamanio()){
                return a2.getTamanio() - a1.getTamanio(); // decreciente
            } else {
                return a1.getNombre().compareTo(a2.getNombre()); // asc por nombre
            }
        });
    }

    public int getCantApp(){ return apps.size(); }
    public String getModelo(){ return modelo; }
    public Pantalla getPantalla(){ return pantalla; }
    public ArrayList<Aplicacion> getApps(){ return apps; }

    @Override
    public String toString() {
        return "Laptop{modelo=" + modelo + ", cantApp=" + cantApp + ", pantalla=" + pantalla + ", apps=" + apps + '}';
    }
}