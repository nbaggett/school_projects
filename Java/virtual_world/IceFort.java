import processing.core.PImage;

import java.util.List;
import java.util.Optional;

public class IceFort extends ActiveEntity
{
    public IceFort(String id, Point position, List<PImage> images, int actionperiod)
    {
        super(id, position, images, actionperiod);
    }

    public void executeActivity(WorldModel world, ImageStore imageStore, EventScheduler scheduler)
    {
        Optional<Point> openPt = world.findOpenAround(super.getPosition());

        if (openPt.isPresent())
        {
            Snowman snowman = new Snowman("snowyboy", openPt.get(), imageStore.getImageList(VirtualWorld.SNOWMAN_KEY), 1000, 250);
            world.addEntity(snowman);
            snowman.scheduleActions(scheduler, world, imageStore);
        }

        scheduler.scheduleEvent(this,
                new Activity(this, world, imageStore),
                super.getActionPeriod());
    }
}
