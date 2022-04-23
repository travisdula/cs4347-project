export function Flight(props: any) {
    const fnum = props.flightNum
    const time = props.departureTime
    const date = props.date
    const destination = props.destination
    return (
        <div className="flex flex-col w-24">
            <div className="title text-xl font-bold text-left">{fnum}</div>
            <div className="flex flex-row flex-auto">
                <span className="text-left text-gray-700 font-semibold"> {destination} </span>
                <span className="text-right flex-grow text-gray-600"> {date} {time}</span>
            </div>
        </div>
    )
}
