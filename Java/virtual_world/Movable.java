import java.util.LinkedList;
import java.util.List;
import java.util.Optional;

public interface Movable
{
    void move(WorldModel world, Point pos);
    void removeAt(WorldModel world, Point pos);
    Point nextPosition(WorldModel world, Point destPos);
    boolean moveTo(EventScheduler scheduler, WorldModel world, Entity target);

    static Optional<Entity> findNearest(WorldModel world, Point pos,
                                                Class<? extends Entity> kind)
    {
        List<Entity> ofType = new LinkedList<>();
        for (Entity entity : world.getEntities())
        {
            if (kind.isInstance(entity))
            {
                ofType.add(entity);
            }
        }

        return nearestEntity(ofType, pos);
    }

    static Optional<Entity> nearestEntity(List<Entity> entities,
                                                  Point pos)
    {
        if (entities.isEmpty())
        {
            return Optional.empty();
        }
        else
        {
            Entity nearest = entities.get(0);
            int nearestDistance = distanceSquared(nearest.getPosition(), pos);

            for (Entity other : entities)
            {
                int otherDistance = distanceSquared(other.getPosition(), pos);

                if (otherDistance < nearestDistance)
                {
                    nearest = other;
                    nearestDistance = otherDistance;
                }
            }

            return Optional.of(nearest);
        }
    }

    static int distanceSquared(Point p1, Point p2)
    {
        int deltaX = p1.getX() - p2.getX();
        int deltaY = p1.getY() - p2.getY();

        return deltaX * deltaX + deltaY * deltaY;
    }

    static boolean adjacent(Point p1, Point p2) {
        return (p1.getX() == p2.getX() && Math.abs(p1.getY() - p2.getY()) == 1) ||
                (p1.getY() == p2.getY() && Math.abs(p1.getX() - p2.getX()) == 1);
    }

    static boolean almostAdjacent(Point p1, Point p2) {
        return (p1.getX() == p2.getX() || Math.abs(p1.getY() - p2.getY()) == 1) ||
                (p1.getY() == p2.getY() || Math.abs(p1.getX() - p2.getX()) == 1);
    }
}
