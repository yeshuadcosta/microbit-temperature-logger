def on_button_pressed_a():
    basic.show_string("" + str(input.temperature()))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global actualtime, time
    music._play_default_background(music.built_in_playable_melody(Melodies.JUMP_UP),
        music.PlaybackMode.IN_BACKGROUND)
    while True:
        # 5 Second Interval
        actualtime = time * timeinterval
        datalogger.log(datalogger.create_cv("Time", actualtime),
            datalogger.create_cv("Temperature", input.temperature()))
        led.plot_bar_graph(time, iterations)
        if time == iterations:
            terminate()
            break
        # Increment once after every iteration
        time += 1
        basic.pause(timeinterval * 1000)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_string("" + str(actualtime))
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    music._play_default_background(music.built_in_playable_melody(Melodies.FUNERAL),
        music.PlaybackMode.IN_BACKGROUND)
    basic.show_icon(IconNames.SKULL)
    datalogger.delete_log(datalogger.DeleteType.FULL)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

# This function should be executed on time duration end
def terminate():
    music._play_default_background(music.built_in_playable_melody(Melodies.RINGTONE),
        music.PlaybackMode.IN_BACKGROUND)
    basic.show_icon(IconNames.CHESSBOARD)
    basic.show_icon(IconNames.DIAMOND)
    basic.show_icon(IconNames.SMALL_DIAMOND)
    basic.show_icon(IconNames.YES)
actualtime = 0
time = 0
iterations = 0
timeinterval = 0
datalogger.include_timestamp(FlashLogTimeStampFormat.NONE)
music.set_built_in_speaker_enabled(True)
music.set_volume(200)
datalogger.set_column_titles("Time", "Temperature")
duration = 300
timeinterval = 20
iterations = duration / timeinterval
time = 0
actualtime = 0