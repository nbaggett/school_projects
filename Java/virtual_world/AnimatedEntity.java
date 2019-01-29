import processing.core.PImage;

import java.util.List;
import java.util.Optional;

public abstract  class AnimatedEntity extends ActiveEntity implements Movable
{
    private int animationPeriod;
    private int imageIndex = 0;

    private PathingStrategy strategy = new AStarPathingStrategy();

    public AnimatedEntity(String id, Point position, List<PImage> images,int actionPeriod, int animationPeriod)
    {
        super(id, position, images, actionPeriod);
        this.animationPeriod = animationPeriod;
    }
    public int getAnimationPeriod()
    {
        return animationPeriod;
    }

    @Override
    public int getImageIndex()
    {
        return imageIndex;
    }

    public void nextImage()
    {
        imageIndex = (imageIndex + 1) % super.getImages().size();
    }

    @Override
    public void scheduleActions(EventScheduler scheduler, WorldModel world, ImageStore imageStore) {
        super.scheduleActions(scheduler, world, imageStore);
        scheduler.scheduleEvent(this, new Animation(this, world, imageStore, 0), animationPeriod);
    }

    public boolean moveTo(EventScheduler scheduler, WorldModel world, Entity target)
    {
        if (Movable.adjacent(super.getPosition(), target.getPosition()))
        {
            if (this.getClass().equals(MinerNotFull.class))
            {
                ((MinerNotFull)this).incrementResource();
            }

            else if(this.getClass().equals(MinerFull.class))
            {
                return true;
            }

            if(this.getClass().equals(IceSoldierNotFull.class))
            {
                ((IceSoldierNotFull)this).incrementMinerCount();
            }

            else if(this.getClass().equals(IceSoldierFull.class))
            {
                return true;
            }
            target.remove(world);
            scheduler.unscheduleAllEvents(target);
            return true;
        }
        else
        {

            Point nextPos = nextPosition(world, target.getPosition());

            if (!super.getPosition().equals(nextPos))
            {
                Optional<Entity> occupant = world.getOccupant(nextPos);
                if (occupant.isPresent())
                {
                    scheduler.unscheduleAllEvents(occupant.get());
                }

                move(world, nextPos);
            }
            return false;
        }
    }

    private static boolean neighbors(Point p1, Point p2)
    {
        return p1.x+1 == p2.x && p1.y == p2.y ||
                p1.x-1 == p2.x && p1.y == p2.y ||
                p1.x == p2.x && p1.y+1 == p2.y ||
                p1.x == p2.x && p1.y-1 == p2.y;
    }

    public void move(WorldModel world, Point pos)
    {
        Point oldPos = this.getPosition();
        if (world.withinBounds(pos) && !pos.equals(oldPos))
        {
            world.setOccupancyCell(oldPos, null);
            removeAt(world, pos);
            world.setOccupancyCell(pos, this);
            super.setPosition(pos);
        }
    }

    public void removeAt(WorldModel world, Point pos)
    {
        if (world.withinBounds(pos)
                && world.getOccupancyCell(pos) != null)
        {
            Entity entity = world.getOccupancyCell(pos);

         /* this moves the entity just outside of the grid for
            debugging purposes */
            super.setPosition(new Point(-1, -1));
            world.entities.remove(entity);
            world.setOccupancyCell(pos, null);
        }
    }

    public Point nextPosition(WorldModel world, Point destPos) {
        List<Point> points;

        points = strategy.computePath(this.getPosition(), destPos,
                p ->  world.withinBounds(p) && !world.isOccupied(p),
                (p1, p2) -> neighbors(p1,p2),
                PathingStrategy.CARDINAL_NEIGHBORS);

        if (points.size() == 0)
        {
            return this.getPosition();
        }
        Point nextPos = points.get(0);
        return nextPos;
    }

    public boolean transformToSnowman(WorldModel world, EventScheduler scheduler, ImageStore imageStore)
    {
        Snowman snowman = new Snowman(super.getId(), super.getPosition(), super.getImages(), super.getActionPeriod(), getAnimationPeriod());

        this.remove(world);
        scheduler.unscheduleAllEvents(this);

        world.addEntity(snowman);
        snowman.scheduleActions(scheduler, world, imageStore);

        return true;
    }
}
