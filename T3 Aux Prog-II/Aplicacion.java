package comp.agrega;

public class Aplicacion {
    private String nombre;
    private int tamanio;

    public Aplicacion(String nombre, int tamanio) {
        this.nombre = nombre;
        this.tamanio = tamanio;
    }
    public Aplicacion() {}

    public String getNombre() { return nombre; }
    public int getTamanio() { return tamanio; }

    @Override
    public String toString() {
        return "Aplicacion{nombre=" + nombre + ", tamanio=" + tamanio + '}';
    }
}