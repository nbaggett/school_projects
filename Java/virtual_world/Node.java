final class Node
{
    public final int g;
    public final int h;
    public final int f;
    public Point vertex;
    public Node prior;

    public Node(int g, int h, Point vertex, Node prior) {
        this.g = g;
        this.h = h;
        this.f = g + h;
        this.vertex = vertex;
        this.prior = prior;
    }

    public int hashCode()
    {
        int result = 0;
        result = result * 31 + ((g == 0)?0:((Integer)g).hashCode());
        result = result * 31 * 31 + ((h == 0)?0:((Integer)h).hashCode());
        result = result * 31 * 31 * 31 + ((f == 0)?0:((Integer)f).hashCode());
        result = result * 31 * 31 * 31 * 31 + ((vertex.x == 0)?0:((Integer)vertex.x).hashCode());
        result = result * 31 * 31 * 31 * 31 * 31 + ((vertex.y == 0)?0:((Integer)vertex.y).hashCode());
        result = result * 31 * 31 * 31 * 31 * 31 * 31 + ((prior == null)?0:((Integer)prior.f).hashCode());
        return result;
    }
}

