import java.util.*;
import java.util.function.BiPredicate;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.stream.Collectors;
import java.util.Comparator;
import java.util.stream.Stream;

class AStarPathingStrategy implements PathingStrategy
{


    public List<Point> computePath(Point start, Point end,
                                   Predicate<Point> canPassThrough,
                                   BiPredicate<Point, Point> withinReach,
                                   Function<Point, Stream<Point>> potentialNeighbors)
    {
        LinkedList<Point> path = new LinkedList<>();
        Comparator<Node> comp = new FComparator();
        PriorityQueue<Node> openList = new PriorityQueue<>(comp);
        Hashtable<Integer, Node> closedList = new Hashtable<>();
        Set<Point> visited = new HashSet<>();

        openList.add(new Node(0, manhattanDistance(start, end), start, null));

        while (openList.size() != 0)
        {
            Node q = openList.poll();

            if (visited.contains(q.vertex))
            {
                continue;
            }

            visited.add(q.vertex);

            List<Point> adjacent = potentialNeighbors.apply(q.vertex)
                                                        .filter(canPassThrough)
                                                        .collect(Collectors.toList());

            if (adjacent.size() == 0)
            {
                visited.add(q.vertex);
                continue;
            }

            List<Node> validNodes = new LinkedList<>();
            for (Point p: adjacent)
            {
                Node no = new Node(manhattanDistance(start, q.vertex) + manhattanDistance(q.vertex, p), manhattanDistance(end, p), p, q);
                if (!closedList.containsKey(no.hashCode()) && !visited.contains(no.vertex))
                {
                    validNodes.add(no);
                }
            }

            for (Node n : validNodes)
            {
                if (withinReach.test(n.vertex, end))
                {
                    Node prev = n.prior;
                    path.addFirst(n.vertex);
                    while (prev.g != 0)
                    {
                        path.addFirst(prev.vertex);
                        prev = prev.prior;
                    }
                    openList.clear();
                    closedList.clear();
                    break;
                }

                if (!openList.contains(n) && !visited.contains(n.vertex))
                {
                    openList.add(n);
                }
            }
            closedList.put(q.hashCode(), q);
        }
        return path;
    }

    private static int manhattanDistance(Point p1, Point p2)
    {
        int dx = p1.x - p2.x;
        int dy = p1.y - p2.y;

        return Math.abs(dx) + Math.abs(dy);
    }
}
