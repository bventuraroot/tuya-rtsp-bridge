# FAQ

### קאַמערע־ליסטע ליידיק נאָך לאָגין
פֿאַלשע רעגיאָן. «מערב־אייראָפּע» אין דער DE־אַפּ = **EU**, ניט WE.

### QR ענדיקט זיך ניט
האַלט דאָס פֿענסטער אָפֿן און **באַשטעטיק** אויפֿן טעלעפֿאָן.

### QR קליין / שפּאַלט / ניט סקענירבאַר (Windows)
פֿאַרריכט אין **1.2.4+**: פֿיקסירט **320×320** קאַנוועס (NEAREST). דערהייַנטיק די אַפּ. «No QR» פֿאַר Create QR איז נאָרמאַל.

### פֿאַרבינדונג אָפּגעזאָגט (WinError 10061)
די UI סטאַרט די API (`:8787`) אַליין. פּרוּוו Create QR נאָך אַ מאָל.

### VLC שוואַרץ
VLC 3 פֿאַלט אָפֿט אויף HEVC/RTSP. דער סטרים לעבט. Agent/Frigate. Linux: ffmpeg MJPEG.

### געוואָלט 60 fps
פֿיל מאָדעלן געבן ~**10 fps** אין HD.

### איז דאָס ONVIF?
ניין. נאָר RTSP.

### גייט ווידעאָ אַרויס פֿון שטוב?
סיגנאַלירונג צו Tuya. לאָקאַל געוויינטלעך קאַמערע → דער PC.

### Cloud PTZ אַרויס פֿון LAN?
ערשט LAN PTZ (TCP **6668**). ווײַט: cloud נאָך email+פּאַראָל איין מאָל (`POST /api/cloud/auth`) — אָן IoT developer keys.

### Home Assistant add-on?
יאָ — [`homeassistant/tuya_rtsp_bridge/`](../../homeassistant/tuya_rtsp_bridge/). Host network. Docker: [docker.md](../docker.md).

### Linux / macOS?
`./launch.sh`. Arch: [arch-linux.md](../arch-linux.md). דאַטן: `~/.local/share/tuya-rtsp-bridge/`.
