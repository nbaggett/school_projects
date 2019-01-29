import java.util.Comparator;

public class FComparator implements Comparator<Node>
{
    public int compare(Node node1, Node node2)
    {
        if (node1.f < node2.f)
        {
            return -1;
        }

        if (node1.f > node2.f)
        {
            return 1;
        }
        return 0;
    }
}
