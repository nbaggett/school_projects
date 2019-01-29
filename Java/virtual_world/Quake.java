import processing.core.PImage;
import java.util.List;

public class Quake extends AnimatedEntity
{
    private static final int QUAKE_ACTION_PERIOD = 1100;
    private static final int QUAKE_ANIMATION_PERIOD = 100;

    public Quake(String id, Point position, List<PImage> images)
    {
        super(id, position, images, QUAKE_ACTION_PERIOD, QUAKE_ANIMATION_PERIOD);
    }

    public void executeActivity(WorldModel world, ImageStore imageStore, EventScheduler scheduler)
    {
        scheduler.unscheduleAllEvents(this);
        remove(world);
    }
}
